"""Client for the Famn realtime gateway.

The gateway streams a paired space's changes over a WebSocket. A session is
authenticated with the device's access token; because those are short lived,
a fresh auth frame on the open socket extends the session in place rather
than forcing a reconnect.

This module is hand written and is not produced by the code generator.
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Awaitable, Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
import logging
import random
from typing import Any

import aiohttp

from .api_client import ApiClient

LOGGER = logging.getLogger(__name__)

# The gateway confirms its subscription before acknowledging, so a slow
# acknowledgement means something is genuinely wrong.
AUTH_TIMEOUT = 10

# aiohttp pings at this interval and drops the connection when the pong stays
# out, catching half-open sockets. The gateway pings every 30 seconds and
# disconnects after 90 seconds of silence.
HEARTBEAT = 30.0

RECONNECT_MIN_DELAY = 5.0
RECONNECT_MAX_DELAY = 300.0
RECONNECT_MAX_DOUBLINGS = 6

# Gateway error codes that mean the session's credentials were rejected.
AUTH_REJECTED_CODES = (401, 403)

#: Returns an access token together with the moment it should be renewed.
TokenProvider = Callable[[], Awaitable[tuple[str, datetime]]]


class RealtimeError(Exception):
    """Raised when the gateway cannot be used as it is."""


@dataclass(frozen=True)
class Connected:
    """The gateway acknowledged the session; the subscription is live.

    Anything that changed while the socket was down was missed, so a
    consumer should reconcile its state when this arrives.
    """


@dataclass(frozen=True)
class Rejected:
    """The gateway refused a token that looked valid to the caller.

    A revoked device or a clock skew between the caller and the server both
    look like this. The caller should treat its cached token as spent, so
    that the next attempt fetches a fresh one instead of retrying into the
    same wall.
    """


@dataclass(frozen=True)
class Event:
    """A change the gateway pushed for the paired space."""

    topic: str | None = None
    action: str | None = None
    space_id: str | None = None
    event_id: str | None = None
    payload: Any = None


Message = Connected | Rejected | Event


@dataclass
class _Backoff:
    """Exponential reconnect delay with jitter."""

    failures: int = field(default=0)

    def reset(self) -> None:
        """Forget earlier failures after a session that worked."""
        self.failures = 0

    def fail(self) -> None:
        """Record a connection that did not produce a usable session."""
        self.failures += 1

    def delay(self) -> float:
        """Return how long to wait before the next attempt."""
        capped = min(self.failures, RECONNECT_MAX_DOUBLINGS)
        return min(
            RECONNECT_MIN_DELAY * 2**capped, RECONNECT_MAX_DELAY
        ) * random.uniform(0.8, 1.2)


class RealtimeClient:
    """Stream the events of a paired space, reconnecting as needed."""

    def __init__(
        self,
        api_client: ApiClient,
        token_provider: TokenProvider,
        *,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
        """Initialize the client.

        `token_provider` returns a currently valid access token together with
        the moment it should be renewed; it is awaited again whenever that
        moment passes, so token rotation stays with the caller.
        """
        self._api_client = api_client
        self._token_provider = token_provider
        self._session = session
        self._url = api_client.base_url.replace("http", "ws", 1) + "/realtime/ws"

    async def listen(self) -> AsyncIterator[Message]:
        """Yield gateway messages until the caller stops consuming them.

        Connection failures are retried with an exponential backoff, so the
        iterator ends only when it is cancelled or when the token provider
        raises — a rejected device cannot be fixed by reconnecting.
        """
        backoff = _Backoff()
        while True:
            healthy = False
            try:
                async for message in self._connect_once():
                    # Only an acknowledged session counts as one that worked;
                    # a rejection must not reset the backoff.
                    healthy = healthy or isinstance(message, Connected)
                    yield message
            except (aiohttp.ClientError, TimeoutError) as err:
                LOGGER.debug("Famn realtime connection failed: %s", err)

            if healthy:
                backoff.reset()
            else:
                backoff.fail()
            await asyncio.sleep(backoff.delay())

    async def _connect_once(self) -> AsyncIterator[Message]:
        """Run a single gateway session, yielding what it pushes."""
        token, renew_at = await self._token_provider()
        session = self._session or aiohttp.ClientSession()
        owns_session = self._session is None

        try:
            async with session.ws_connect(self._url, heartbeat=HEARTBEAT) as ws:
                await ws.send_json({"type": "auth", "token": token})
                async with asyncio.timeout(AUTH_TIMEOUT):
                    if not await self._await_auth_ok(ws):
                        yield Rejected()
                        return

                LOGGER.debug("Connected to the Famn realtime gateway")
                yield Connected()

                async for message in self._read(ws, renew_at):
                    yield message
        finally:
            if owns_session:
                await session.close()

    async def _await_auth_ok(self, ws: aiohttp.ClientWebSocketResponse) -> bool:
        """Wait for the gateway to acknowledge the auth frame."""
        message = await ws.receive()
        if message.type is not aiohttp.WSMsgType.TEXT:
            return False

        data: dict[str, Any] = message.json()
        if data.get("type") == "auth_ok":
            return True

        LOGGER.debug("Famn realtime gateway rejected the session: %s", data)
        return False

    async def _read(
        self, ws: aiohttp.ClientWebSocketResponse, renew_at: datetime
    ) -> AsyncIterator[Message]:
        """Forward events until the session ends.

        Rather than a second timer task, the receive timeout doubles as the
        renewal schedule: when the deadline passes, a fresh auth frame
        extends the session in place.
        """
        renewed = False
        while True:
            remaining = (renew_at - datetime.now(timezone.utc)).total_seconds()
            if remaining <= 0:
                if renewed:
                    # The token just fetched is already due for renewal, so
                    # the deadline is not advancing — a server clock ahead of
                    # ours, or an expiry echoed back unchanged. Renewing
                    # again would spin against the gateway at full speed.
                    raise RealtimeError(
                        "Famn returned an access token that is already due for renewal"
                    )
                token, renew_at = await self._token_provider()
                await ws.send_json({"type": "auth", "token": token})
                renewed = True
                continue
            renewed = False

            try:
                async with asyncio.timeout(remaining):
                    message = await ws.receive()
            except TimeoutError:
                # Renewal deadline reached; loop back for a fresh token.
                continue

            if message.type in (
                aiohttp.WSMsgType.CLOSE,
                aiohttp.WSMsgType.CLOSING,
                aiohttp.WSMsgType.CLOSED,
                aiohttp.WSMsgType.ERROR,
            ):
                return
            if message.type is not aiohttp.WSMsgType.TEXT:
                continue

            data: dict[str, Any] = message.json()
            match data.get("type"):
                case "event":
                    yield Event(
                        topic=data.get("topic"),
                        action=data.get("action"),
                        space_id=data.get("spaceId"),
                        event_id=data.get("eventId"),
                        payload=data.get("payload"),
                    )
                case "error":
                    LOGGER.debug("Famn realtime gateway error: %s", data)
                    if data.get("code") in AUTH_REJECTED_CODES:
                        # The session is dead; reconnect with a fresh token.
                        yield Rejected()
                        return
                case _:
                    # auth_ok for renewals, pong, and future frame types.
                    pass

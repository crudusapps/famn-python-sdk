# famn-sdk

Swagger API client

This asynchronous Python SDK was generated from Swagger API version 1.0.2.
It uses `aiohttp` and can reuse the session managed by Home Assistant.

## Installation

```bash
pip install .
```

## Usage

```python
from famn_sdk import ApiClient

async def example(session):
    client = ApiClient(session=session)
    # api = SomeApi(client)
    # result = await api.some_operation(...)
```

An injected `aiohttp.ClientSession` remains owned by the caller. If no session
is supplied, use `async with ApiClient() as client:` so the generated client
closes the session it creates.

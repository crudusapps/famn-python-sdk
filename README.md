# famnsdk

Async Python client for the [Famn](https://famn.app) family organizer API.

Generated from the Famn OpenAPI description. It uses `aiohttp` and can reuse a
session owned by the caller, which is how the Home Assistant integration
consumes it.

## Installation

```bash
pip install famnsdk
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

## Regenerating

The generator rewrites `README.md`, `pyproject.toml`, `config.json`,
`.gitignore`, `src/famn_sdk/__init__.py`, `src/famn_sdk/apis.py` and
`src/famn_sdk/models.py`. Three things in this repository are hand written and
are not reproduced by it:

- `src/famn_sdk/realtime.py`, the WebSocket gateway client. It is not a file
  the generator writes, so it survives — but nothing in the generated
  `__init__.py` re-exports it. Import it from the submodule
  (`from famn_sdk.realtime import RealtimeClient`), never from the package
  root, so a regenerate cannot break callers.
- The packaging metadata in `pyproject.toml`: `license`, `license-files`,
  the real `description`, the classifiers and `[project.urls]`. A regenerate
  drops these back to the generator's defaults, and a release published
  without them is not usable as a Home Assistant dependency.

- The build-artifact rules in `.gitignore` (`build/`, `dist/`, `*.egg-info/`),
  without which a local `python -m build` leaves output that looks committable.

Run `python scripts/check_handwritten.py` after regenerating; CI runs it too.

## Releasing

Releases are published to PyPI by the `Upload Python Package` GitHub Actions
workflow, using PyPI trusted publishing, when a GitHub release is created.
Bump `version` in `pyproject.toml`, `__version__` in `src/famn_sdk/__init__.py`
and `packageVersion` in `config.json`, then tag and publish the release.

## License

[MIT](LICENSE)

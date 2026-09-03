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

## Releasing

Releases are published to PyPI by the `Upload Python Package` GitHub Actions
workflow, using PyPI trusted publishing, when a GitHub release is created.
Bump `version` in `pyproject.toml`, `__version__` in `src/famn_sdk/__init__.py`
and `packageVersion` in `config.json`, then tag and publish the release.

## License

[MIT](LICENSE)

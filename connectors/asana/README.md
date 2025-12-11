# Airbyte Asana AI Connector

Type-safe Asana API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-asana
```

## Usage

```python
from airbyte_ai_asana import AsanaConnector
from airbyte_ai_asana.models import AsanaAuthConfig

connector = AsanaConnector(auth_config=AsanaAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
result = connector.tasks.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Asana API Reference](https://developers.asana.com/reference/rest-api-reference).

## Version Information

**Package Version:** 0.19.5

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 11427ac330c199db4b55578f96eb18ab6474610e
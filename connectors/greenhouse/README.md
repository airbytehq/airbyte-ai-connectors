# Airbyte Greenhouse AI Connector

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-greenhouse
```

## Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector
from airbyte_ai_greenhouse.models import GreenhouseAuthConfig

connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))result = connector.candidates.list()```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Greenhouse API Reference](https://developers.greenhouse.io/harvest.html).

## Version Information

**Package Version:** 0.17.4

**Connector Version:** 0.1.0

**Generated with connector-sdk:** bdd5df6d00c95fe27bf5a01652296763fbc05614
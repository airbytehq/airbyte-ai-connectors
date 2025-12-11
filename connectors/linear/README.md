# Airbyte Linear AI Connector

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-linear
```

## Usage

```python
from airbyte_ai_linear import LinearConnector
from airbyte_ai_linear.models import LinearAuthConfig

connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
result = connector.issues.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Linear API Reference](https://linear.app/developers/graphql).

## Version Information

**Package Version:** 0.19.6

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 8c06aa103e1f805b2e8fad3f0ba7004db3d2773a
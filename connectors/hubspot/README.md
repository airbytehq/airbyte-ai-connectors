# Airbyte Hubspot AI Connector

Type-safe Hubspot API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-hubspot
```

## Usage

```python
from airbyte_ai_hubspot import HubspotConnector
from airbyte_ai_hubspot.models import HubspotAuthConfig

# Create connector
connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))

# Use typed methods with full IDE autocomplete
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Hubspot API Reference](https://developers.hubspot.com/docs/api/crm/understanding-the-crm).

## Version Information

**Package Version:** 0.15.4

**Connector Version:** 0.1.1

**Generated with connector-sdk:** f2497f7128da08585d1470953e773671d33f348f
# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector
from airbyte_ai_stripe.models import StripeAuthConfig

# Create connector
connector = StripeConnector(auth_config=StripeAuthConfig(token="..."))

# Use typed methods with full IDE autocomplete
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Stripe API Reference](https://docs.stripe.com/api).

## Version Information

**Package Version:** 0.5.3

**Connector Version:** 0.1.0

**Generated with connector-sdk:** f2497f7128da08585d1470953e773671d33f348f
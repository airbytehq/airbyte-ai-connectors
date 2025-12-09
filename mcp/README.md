# Airbyte Agent MCP Server

MCP server that exposes the Airbyte Connector SDK as Model Context Protocol tools.

## Features

- **Execute**: Run operations on any connector (primary tool)
- **List Entities**: Discover available entities in a connector
- **Describe Entity**: Get detailed schema for an entity
- **Validate Operation**: Check parameters before execution

## Configuration

### 1. Create configured_connectors.yaml

```yaml
# Connector definitions
connectors:
  - id: stripe
    type: local
    path: ../integrations/stripe/connector.yaml
    description: "My Stripe API connector"
    secrets:
      api_key: STRIPE_API_KEY
```

`configured_connectors.yaml.example` contains an example of how to configure connectors.

### 2. Create .env file

```bash
STRIPE_API_KEY=sk_test_your_stripe_api_key_here
```

## Running

```bash
uv run airbyte_agent_mcp
```

The server also takes in args for specific paths to the configured_connectors.yaml file and the env file. With custom paths:

```bash
python -m airbyte_agent_mcp path/to/configured_connectors.yaml path/to/.env
```

The default paths are `./configured_connectors.yaml` and `./.env`

## Usage with Claude Code

Add to `~/.claude.json`:

```json
"mcpServers": {
  "airbyte-agent-mcp": {
    "type": "stdio",
    "command": "uv",
    "args": [
      "--directory",
      "/path/to/sonar/connector-mcp",
      "run",
      "airbyte_agent_mcp"
    ],
    "env": {}
  }
},
```

## Development / Testing

```bash
# Install dev dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Format code
uv run ruff format .

# Lint code
uv run ruff check .
```

# AI Connectors

This repository contains auto-generated Python connector packages for Airbyte AI integrations. These connectors are designed to interface directly with AI Agents to quickly fetch data from external services on-demand. These connectors can be made available to your agents via Python SDK, MCP (coming soon) or API (coming soon).

## Python SDK Example Installation

The Python SDK exposes Airbyte AI Connectors as native Python clients. These can run standalone or be attached as tools inside frameworks like PydanticAI or LangChain. To get started, add the connector package to your dependencies or `pyproject.toml`. For this installation, we will use Gong as an example:

```yaml
dependencies = [
    "pydantic-ai>=0.0.1",
    "airbyte-ai-gong",
]
```

Next, import the generated connector class for the integration you plan to use. Provide the necessary API credentials or secrets required by the third-party integration. Airbyte AI Connectors validate these, then expose typed methods for all operations:

```py
from airbyte_ai_gong import GongConnector

connector = GongConnector.create(secrets={
    "access_key": "...",
    "access_key_secret": "...",
})
```

Once this is done, you may attach connector calls as tools so your agent can call them during reasoning or tool execution. See the following example using a PydanticAI Agent:

```py
import os
from pydantic_ai import Agent
from airbyte_ai_gong import GongConnector

connector = GongConnector(auth_config={
    "access_key": os.environ["GONG_ACCESS_KEY"],
    "access_key_secret": os.environ["GONG_ACCESS_KEY_SECRET"],
})

agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You manage Gong calls and transcripts. "
        "You can list users, get user details, list calls, and fetch call details. "
        "Execute actions immediately."
    ),
)

@agent.tool_plain
async def list_users(limit: int = 10):
    return await connector.users.list(limit=limit)

@agent.tool_plain
async def get_user(user_id: str):
    return await connector.users.get(id=user_id)
```

You can see a detailed list of supported entities and methods for each connector by navigating to its [available operations](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/gong#available-operations).

## Connector Structure

Each connector is a standalone Python package:

```
connectors/
├── stripe/
│   ├── airbyte_ai_stripe/
│   ├── pyproject.toml
│   ├── CHANGELOG.md
│   └── README.md
├── github/
│   └── ...
└── ...
```

# Airbyte Gong AI Connector

Gong is a revenue intelligence platform that captures and analyzes customer interactions
across calls, emails, and web conferences. This connector provides access to users,
recorded calls with transcripts, activity statistics, scorecards, trackers, workspaces,
coaching metrics, and library content for sales performance analysis and revenue insights.


## Example Questions

- List all users in my Gong account
- Show me calls from last week
- Get the transcript for call abc123
- What are the activity stats for our sales team?
- List all workspaces in Gong
- Show me the scorecard configurations
- What trackers are set up in my account?
- Get coaching metrics for manager user123

## Unsupported Questions

- Create a new user in Gong
- Delete a call recording
- Update scorecard questions
- Schedule a new meeting
- Send feedback to a team member
- Modify tracker keywords

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector
from airbyte_ai_gong.models import GongAuthConfig

connector = GongConnector(auth_config=GongAuthConfig(access_key="...", access_key_secret="..."))
result = connector.users.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Gong API Reference](https://gong.app.gong.io/settings/api/documentation).

## Version Information

**Package Version:** 0.19.8

**Connector Version:** 0.1.2

**Generated with connector-sdk:** 751920d7d87375c9077a6017ec408309116bff27
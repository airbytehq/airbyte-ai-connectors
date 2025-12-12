# Airbyte Asana AI Connector

Connector for Asana API

## Installation

```bash
uv pip install airbyte-ai-asana
```

## Usage

```python
from airbyte_ai_asana import AsanaConnector, AsanaAuthConfig

connector = AsanaConnector(
  auth_config=AsanaAuthConfig(
    access_token="...",
    refresh_token="...",
    client_id="...",
    client_secret="..."
  )
)
result = connector.tasks.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Tasks | [List](./REFERENCE.md#tasks-list), [Get](./REFERENCE.md#tasks-get) |
| Project Tasks | [List](./REFERENCE.md#project-tasks-list) |
| Workspace Task Search | [List](./REFERENCE.md#workspace-task-search-list) |
| Projects | [List](./REFERENCE.md#projects-list), [Get](./REFERENCE.md#projects-get) |
| Task Projects | [List](./REFERENCE.md#task-projects-list) |
| Team Projects | [List](./REFERENCE.md#team-projects-list) |
| Workspace Projects | [List](./REFERENCE.md#workspace-projects-list) |
| Workspaces | [List](./REFERENCE.md#workspaces-list), [Get](./REFERENCE.md#workspaces-get) |
| Users | [List](./REFERENCE.md#users-list), [Get](./REFERENCE.md#users-get) |
| Workspace Users | [List](./REFERENCE.md#workspace-users-list) |
| Team Users | [List](./REFERENCE.md#team-users-list) |
| Teams | [Get](./REFERENCE.md#teams-get) |
| Workspace Teams | [List](./REFERENCE.md#workspace-teams-list) |
| User Teams | [List](./REFERENCE.md#user-teams-list) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Asana API Reference](https://developers.asana.com/reference/rest-api-reference).

## Version Information

**Package Version:** 0.19.8

**Connector Version:** 0.1.0

**Generated with connector-sdk:** dc79dc8b685e9d8cb980ea80f12595e31c88fdf7
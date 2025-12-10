# Airbyte Asana AI Connector

Type-safe Asana API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.19.1

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-asana
```

## Usage

```python
from airbyte_ai_asana import AsanaConnector
from airbyte_ai_asana.models import AsanaAuthConfig

# Create connector
connector = AsanaConnector(auth_config=AsanaAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Tasks Operations
- `list_tasks()` - Returns a paginated list of tasks
- `get_task()` - Get a single task by its ID

### Project_Tasks Operations
- `list_project_tasks()` - Returns all tasks in a project

### Workspace_Task_Search Operations
- `search_workspace_tasks()` - Returns tasks that match the specified search criteria. Note - This endpoint requires a premium Asana account.

### Projects Operations
- `list_projects()` - Returns a paginated list of projects
- `get_project()` - Get a single project by its ID

### Task_Projects Operations
- `list_task_projects()` - Returns all projects a task is in

### Team_Projects Operations
- `list_team_projects()` - Returns all projects for a team

### Workspace_Projects Operations
- `list_workspace_projects()` - Returns all projects in a workspace

### Workspaces Operations
- `list_workspaces()` - Returns a paginated list of workspaces
- `get_workspace()` - Get a single workspace by its ID

### Users Operations
- `list_users()` - Returns a paginated list of users
- `get_user()` - Get a single user by their ID

### Workspace_Users Operations
- `list_workspace_users()` - Returns all users in a workspace

### Team_Users Operations
- `list_team_users()` - Returns all users in a team

### Teams Operations
- `get_team()` - Get a single team by its ID

### Workspace_Teams Operations
- `list_workspace_teams()` - Returns all teams in a workspace

### User_Teams Operations
- `list_user_teams()` - Returns all teams a user is a member of

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_asana.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.

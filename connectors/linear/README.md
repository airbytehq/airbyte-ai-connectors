# Airbyte Linear AI Connector

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.20.0

**Connector Version:** 0.2.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-linear
```

## Usage

```python
from airbyte_ai_linear import LinearConnector
from airbyte_ai_linear.models import LinearAuthConfig

# Create connector
connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))

# List issues with server-side filtering
issues = await connector.issues.listFiltered(
    stateName="In Progress",
    priority=2,  # High priority
    createdAfter="2025-01-01T00:00:00Z"
)

# Get current user and their issues
viewer = await connector.users.me()

# Access sprint/cycle data
active_cycle = await connector.cycles.getActive(teamId="team-id")

# Get comments on an issue
comments = await connector.comments.list(issueId="issue-id")
```

## Available Operations

### Issues Operations
- `connector.issues.list()` - List all issues with expanded fields (labels, cycle, parent/children, relations)
- `connector.issues.listFiltered()` - List issues with server-side filtering by:
  - `assigneeId` - Filter by assignee
  - `teamId` - Filter by team
  - `stateId` / `stateName` - Filter by workflow state
  - `priority` - Filter by priority (0-4)
  - `labelIds` - Filter by labels
  - `createdAfter` / `createdBefore` - Filter by creation date
  - `updatedAfter` / `updatedBefore` - Filter by update date
  - `cycleId` - Filter by cycle/sprint
  - `projectId` - Filter by project
- `connector.issues.get(id)` - Get issue details including comments and relations

### Comments Operations
- `connector.comments.list(issueId)` - List comments for an issue
- `connector.comments.get(id)` - Get a specific comment

### Cycles (Sprints) Operations
- `connector.cycles.list()` - List all cycles
- `connector.cycles.get(id)` - Get cycle details with issues
- `connector.cycles.getActive(teamId)` - Get current active cycle for a team

### Users Operations
- `connector.users.list()` - List all users
- `connector.users.get(id)` - Get user details with assigned issues
- `connector.users.me()` - Get current authenticated user

### Labels Operations
- `connector.labels.list()` - List all labels
- `connector.labels.get(id)` - Get label details with associated issues

### Workflow States Operations
- `connector.workflowStates.list()` - List workflow states (Todo, In Progress, Done, etc.)

### Projects Operations
- `connector.projects.list()` - List projects with progress and teams
- `connector.projects.get(id)` - Get project details with issues

### Teams Operations
- `connector.teams.list()` - List teams with members and active cycle
- `connector.teams.get(id)` - Get team details with labels and workflow states

## Issue Fields

Issues now include expanded fields:
- `identifier` - Human-readable ID (e.g., ABC-123)
- `labels` - Associated labels
- `cycle` - Associated cycle/sprint
- `parent` - Parent issue
- `children` - Child/sub issues
- `relations` - Blocking/blocked/related issues
- `dueDate` - Due date
- `estimate` - Issue estimate
- `completedAt` / `canceledAt` - Completion timestamps
- `comments` - Issue comments (in get requests)

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_linear.types`.

## Documentation

Generated from OpenAPI 3.0 specification with Airbyte extensions.

For API documentation, see:
- [Linear API Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference)

"""
Type definitions for asana connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class TasksListNextPage(TypedDict):
    """Nested schema for TasksList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class ProjectsListNextPage(TypedDict):
    """Nested schema for ProjectsList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class WorkspacesListNextPage(TypedDict):
    """Nested schema for WorkspacesList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class UsersListNextPage(TypedDict):
    """Nested schema for UsersList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    project_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    task_gid: str

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    workspace: NotRequired[str]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    project_gid: str

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class WorkspacesGetParams(TypedDict):
    """Parameters for workspaces.get operation"""
    workspace_gid: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    workspace: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_gid: str

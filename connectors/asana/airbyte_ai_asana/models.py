"""
Pydantic models for asana connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class AsanaAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Authentication bearer token"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Task(BaseModel):
    """Compact task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class TaskResponse(BaseModel):
    """Task response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Task, Any] = Field(default=None)

class TasksListNextPage(BaseModel):
    """Nested schema for TasksList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class TasksList(BaseModel):
    """Paginated list of tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Task], Any] = Field(default=None)
    next_page: Union[TasksListNextPage | None, Any] = Field(default=None)

class Project(BaseModel):
    """Compact project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class ProjectResponse(BaseModel):
    """Project response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Project, Any] = Field(default=None)

class ProjectsListNextPage(BaseModel):
    """Nested schema for ProjectsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Project], Any] = Field(default=None)
    next_page: Union[ProjectsListNextPage | None, Any] = Field(default=None)

class Workspace(BaseModel):
    """Compact workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class WorkspaceResponse(BaseModel):
    """Workspace response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Workspace, Any] = Field(default=None)

class WorkspacesListNextPage(BaseModel):
    """Nested schema for WorkspacesList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class WorkspacesList(BaseModel):
    """Paginated list of workspaces"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Workspace], Any] = Field(default=None)
    next_page: Union[WorkspacesListNextPage | None, Any] = Field(default=None)

class User(BaseModel):
    """Compact user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class UserResponse(BaseModel):
    """User response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[User, Any] = Field(default=None)

class UsersListNextPage(BaseModel):
    """Nested schema for UsersList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class UsersList(BaseModel):
    """Paginated list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[User], Any] = Field(default=None)
    next_page: Union[UsersListNextPage | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class AsanaExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AsanaExecuteResultWithMeta(AsanaExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.


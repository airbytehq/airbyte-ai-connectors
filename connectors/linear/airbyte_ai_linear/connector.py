"""
linear connector.

Expanded version with support for:
- Server-side filtering for issues
- Comments, Cycles, Users, Labels, WorkflowStates entities
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    IssuesGetParams,
    IssuesListParams,
    ProjectsGetParams,
    ProjectsListParams,
    TeamsGetParams,
    TeamsListParams,
)

if TYPE_CHECKING:
    from .models import LinearAuthConfig

# Import response models and envelope models at runtime
from .models import (
    LinearExecuteResult,
    LinearExecuteResultWithMeta,
    IssueResponse,
    IssuesListResponse,
    ProjectResponse,
    ProjectsListResponse,
    TeamResponse,
    TeamsListResponse,
)


class LinearConnector:
    """
    Type-safe Linear API connector.

    Auto-generated from OpenAPI specification with full type safety.
    Expanded with additional entities: comments, cycles, users, labels, workflowStates.
    """

    connector_name = "linear"
    connector_version = "0.2.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        # Issues
        ("issues", "list"): False,
        ("issues", "search"): False,  # listFiltered uses search action
        ("issues", "get"): False,
        # Projects
        ("projects", "list"): False,
        ("projects", "get"): False,
        # Teams
        ("teams", "list"): False,
        ("teams", "get"): False,
        # Comments
        ("comments", "list"): False,
        ("comments", "get"): False,
        # Cycles
        ("cycles", "list"): False,
        ("cycles", "get"): False,
        ("activeCycle", "get"): False,
        # Users
        ("users", "list"): False,
        ("users", "get"): False,
        # Viewer (current user)
        ("viewer", "get"): False,
        # Labels
        ("labels", "list"): False,
        ("labels", "get"): False,
        # Workflow States
        ("workflowStates", "list"): False,
    }

    def __init__(
        self,
        auth_config: LinearAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new linear connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            airbyte_connector_api_url: Airbyte connector API URL (defaults to Airbyte Cloud API URL)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = LinearConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = LinearConnector(
                auth_config=LinearAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            if not config_path:
                config_path = str(self.get_default_config_path())

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.issues = IssuesQuery(self)
        self.projects = ProjectsQuery(self)
        self.teams = TeamsQuery(self)
        # New entities
        self.comments = CommentsQuery(self)
        self.cycles = CyclesQuery(self)
        self.users = UsersQuery(self)
        self.labels = LabelsQuery(self)
        self.workflowStates = WorkflowStatesQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["list"],
        params: "IssuesListParams"
    ) -> "IssuesListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["get"],
        params: "IssuesGetParams"
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["get"],
        params: "ProjectsGetParams"
    ) -> "ProjectResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "TeamResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> LinearExecuteResult[Any] | LinearExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return LinearExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return LinearExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data


# =============================================================================
# ISSUES QUERY
# =============================================================================

class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> IssuesListResponse:
        """
        Returns a paginated list of issues via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            IssuesListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        return result

    async def listFiltered(
        self,
        first: int | None = None,
        after: str | None = None,
        assigneeId: str | None = None,
        teamId: str | None = None,
        stateId: str | None = None,
        stateName: str | None = None,
        priority: int | None = None,
        labelIds: str | None = None,
        createdAfter: str | None = None,
        createdBefore: str | None = None,
        updatedAfter: str | None = None,
        updatedBefore: str | None = None,
        cycleId: str | None = None,
        projectId: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns a filtered list of issues with server-side filtering.

        Args:
            first: Number of items to return (max 250)
            after: Cursor for pagination
            assigneeId: Filter by assignee user ID
            teamId: Filter by team ID
            stateId: Filter by workflow state ID
            stateName: Filter by workflow state name (e.g., "In Progress", "Todo")
            priority: Filter by priority (0=No priority, 1=Urgent, 2=High, 3=Normal, 4=Low)
            labelIds: Filter by label IDs (comma-separated)
            createdAfter: Filter issues created after this date (ISO 8601)
            createdBefore: Filter issues created before this date (ISO 8601)
            updatedAfter: Filter issues updated after this date (ISO 8601)
            updatedBefore: Filter issues updated before this date (ISO 8601)
            cycleId: Filter by cycle/sprint ID
            projectId: Filter by project ID
            **kwargs: Additional parameters

        Returns:
            Filtered issues list response
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            "assigneeId": assigneeId,
            "teamId": teamId,
            "stateId": stateId,
            "stateName": stateName,
            "priority": priority,
            "labelIds": labelIds,
            "createdAfter": createdAfter,
            "createdBefore": createdBefore,
            "updatedAfter": updatedAfter,
            "updatedBefore": updatedBefore,
            "cycleId": cycleId,
            "projectId": projectId,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "search", params)
        return result

    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Get a single issue by ID via GraphQL

        Args:
            id: Issue ID
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result


# =============================================================================
# COMMENTS QUERY
# =============================================================================

class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        issueId: str,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns comments for a specific issue.

        Args:
            issueId: The issue ID to get comments for
            first: Number of comments to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            Comments list response
        """
        params = {k: v for k, v in {
            "issueId": issueId,
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        return result

    async def get(
        self,
        id: str,
        **kwargs
    ) -> Any:
        """
        Get a single comment by ID.

        Args:
            id: Comment ID
            **kwargs: Additional parameters

        Returns:
            Comment response
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        return result


# =============================================================================
# CYCLES QUERY
# =============================================================================

class CyclesQuery:
    """
    Query class for Cycles (sprints) entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        teamId: str | None = None,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns a list of cycles (sprints).

        Args:
            teamId: Filter by team ID
            first: Number of cycles to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            Cycles list response
        """
        params = {k: v for k, v in {
            "teamId": teamId,
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cycles", "list", params)
        return result

    async def get(
        self,
        id: str,
        **kwargs
    ) -> Any:
        """
        Get a single cycle by ID with its issues.

        Args:
            id: Cycle ID
            **kwargs: Additional parameters

        Returns:
            Cycle response
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cycles", "get", params)
        return result

    async def getActive(
        self,
        teamId: str,
        **kwargs
    ) -> Any:
        """
        Get the currently active cycle for a team.

        Args:
            teamId: Team ID
            **kwargs: Additional parameters

        Returns:
            Active cycle response
        """
        params = {k: v for k, v in {
            "teamId": teamId,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("activeCycle", "get", params)
        return result


# =============================================================================
# USERS QUERY
# =============================================================================

class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns a list of users in the organization.

        Args:
            first: Number of users to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            Users list response
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        return result

    async def get(
        self,
        id: str,
        **kwargs
    ) -> Any:
        """
        Get a single user by ID with their assigned issues.

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            User response
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result

    async def me(self, **kwargs) -> Any:
        """
        Get the currently authenticated user (viewer).

        Args:
            **kwargs: Additional parameters

        Returns:
            Viewer response with assigned issues and team memberships
        """
        params = {k: v for k, v in kwargs.items() if v is not None}

        result = await self._connector.execute("viewer", "get", params)
        return result


# =============================================================================
# LABELS QUERY
# =============================================================================

class LabelsQuery:
    """
    Query class for Labels entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        teamId: str | None = None,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns a list of labels.

        Args:
            teamId: Filter by team ID
            first: Number of labels to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            Labels list response
        """
        params = {k: v for k, v in {
            "teamId": teamId,
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "list", params)
        return result

    async def get(
        self,
        id: str,
        **kwargs
    ) -> Any:
        """
        Get a single label by ID with its associated issues.

        Args:
            id: Label ID
            **kwargs: Additional parameters

        Returns:
            Label response
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "get", params)
        return result


# =============================================================================
# WORKFLOW STATES QUERY
# =============================================================================

class WorkflowStatesQuery:
    """
    Query class for Workflow States entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        teamId: str | None = None,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> Any:
        """
        Returns a list of workflow states (Todo, In Progress, Done, etc.).

        Args:
            teamId: Filter by team ID
            first: Number of states to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            Workflow states list response
        """
        params = {k: v for k, v in {
            "teamId": teamId,
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workflowStates", "list", params)
        return result


# =============================================================================
# PROJECTS QUERY
# =============================================================================

class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> ProjectsListResponse:
        """
        Returns a paginated list of projects via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            ProjectsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        return result


    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProjectResponse:
        """
        Get a single project by ID via GraphQL

        Args:
            id: Project ID
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result


# =============================================================================
# TEAMS QUERY
# =============================================================================

class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> TeamsListResponse:
        """
        Returns a list of teams via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            TeamsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        return result


    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> TeamResponse:
        """
        Get a single team by ID via GraphQL

        Args:
            id: Team ID
            **kwargs: Additional parameters

        Returns:
            TeamResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result

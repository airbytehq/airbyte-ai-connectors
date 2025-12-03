"""
Auto-generated gong connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from ._vendored.connector_sdk import save_download

if TYPE_CHECKING:
    from .types import (
        ActivityAggregateResponse,
        ActivityDayByDayResponse,
        AsyncIterator,
        CallAudioDownloadParams,
        CallResponse,
        CallTranscriptsListParams,
        CallVideoDownloadParams,
        CallsExtensiveListParams,
        CallsGetParams,
        CallsListParams,
        CallsResponse,
        ExtensiveCallsResponse,
        InteractionStatsResponse,
        StatsActivityAggregateListParams,
        StatsActivityDayByDayListParams,
        StatsInteractionListParams,
        TranscriptsResponse,
        UserResponse,
        UsersGetParams,
        UsersListParams,
        UsersResponse,
        WorkspacesListParams,
        WorkspacesResponse,
        GongAuthConfig,
    )


class GongConnector:
    """
    Type-safe Gong API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "gong"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(
        self,
        auth_config: GongAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new gong connector instance.

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
            connector = GongConnector(auth_config={"api_key": "sk_..."})
            # Hosted mode (executed on Airbyte cloud)
            connector = GongConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GongConnector(
                auth_config={"access_token": "...", "refresh_token": "..."},
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
                auth_config=auth_config,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.users = UsersQuery(self)
        self.calls = CallsQuery(self)
        self.calls_extensive = CallsExtensiveQuery(self)
        self.call_audio = CallAudioQuery(self)
        self.call_video = CallVideoQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.call_transcripts = CallTranscriptsQuery(self)
        self.stats_activity_aggregate = StatsActivityAggregateQuery(self)
        self.stats_activity_day_by_day = StatsActivityDayByDayQuery(self)
        self.stats_interaction = StatsInteractionQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "UserResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["list"],
        params: "CallsListParams"
    ) -> "CallsResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["get"],
        params: "CallsGetParams"
    ) -> "CallResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls_extensive"],
        action: Literal["list"],
        params: "CallsExtensiveListParams"
    ) -> "ExtensiveCallsResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["call_audio"],
        action: Literal["download"],
        params: "CallAudioDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["call_video"],
        action: Literal["download"],
        params: "CallVideoDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspaces"],
        action: Literal["list"],
        params: "WorkspacesListParams"
    ) -> "WorkspacesResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["call_transcripts"],
        action: Literal["list"],
        params: "CallTranscriptsListParams"
    ) -> "TranscriptsResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_activity_aggregate"],
        action: Literal["list"],
        params: "StatsActivityAggregateListParams"
    ) -> "ActivityAggregateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_activity_day_by_day"],
        action: Literal["list"],
        params: "StatsActivityDayByDayListParams"
    ) -> "ActivityDayByDayResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_interaction"],
        action: Literal["list"],
        params: "StatsInteractionListParams"
    ) -> "InteractionStatsResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> dict[str, Any]: ...

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

        return result.data



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> UsersResponse:
        """
        List users

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            UsersResponse
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> UserResponse:
        """
        Get a user

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            UserResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "get", params)



class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        from_date_time: str,
        to_date_time: str,
        cursor: str | None = None,
        **kwargs
    ) -> CallsResponse:
        """
        List calls

        Args:
            from_date_time: Start date in ISO 8601 format
            to_date_time: End date in ISO 8601 format
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsResponse
        """
        params = {k: v for k, v in {
            "fromDateTime": fromDateTime,
            "toDateTime": toDateTime,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> CallResponse:
        """
        Get a call

        Args:
            id: Call ID
            **kwargs: Additional parameters

        Returns:
            CallResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls", "get", params)



class CallsExtensiveQuery:
    """
    Query class for CallsExtensive entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ExtensiveCallsResponse:
        """
        List calls with extensive data

        Returns:
            ExtensiveCallsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls_extensive", "list", params)



class CallAudioQuery:
    """
    Query class for CallAudio entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Download call audio

        Args:
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_audio", "download", params)


    async def download_local(
        self,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Download call audio and save to file.

        Args:
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """

        # Get the async iterator
        params = cast(CallAudioDownloadParams, {k: v for k, v in {
            "range_header": range_header,
            **kwargs
        }.items() if v is not None})

        content_iterator = await self._connector.execute("", "", params)

        return await save_download(content_iterator, path)


class CallVideoQuery:
    """
    Query class for CallVideo entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Download call video

        Args:
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_video", "download", params)


    async def download_local(
        self,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Download call video and save to file.

        Args:
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """

        # Get the async iterator
        params = cast(CallVideoDownloadParams, {k: v for k, v in {
            "range_header": range_header,
            **kwargs
        }.items() if v is not None})

        content_iterator = await self._connector.execute("", "", params)

        return await save_download(content_iterator, path)


class WorkspacesQuery:
    """
    Query class for Workspaces entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> WorkspacesResponse:
        """
        List workspaces

        Returns:
            WorkspacesResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("workspaces", "list", params)



class CallTranscriptsQuery:
    """
    Query class for CallTranscripts entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TranscriptsResponse:
        """
        Retrieve call transcripts

        Returns:
            TranscriptsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_transcripts", "list", params)



class StatsActivityAggregateQuery:
    """
    Query class for StatsActivityAggregate entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ActivityAggregateResponse:
        """
        Retrieve aggregated activity statistics

        Returns:
            ActivityAggregateResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_aggregate", "list", params)



class StatsActivityDayByDayQuery:
    """
    Query class for StatsActivityDayByDay entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ActivityDayByDayResponse:
        """
        Retrieve daily activity statistics

        Returns:
            ActivityDayByDayResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_day_by_day", "list", params)



class StatsInteractionQuery:
    """
    Query class for StatsInteraction entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> InteractionStatsResponse:
        """
        Retrieve interaction statistics

        Returns:
            InteractionStatsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_interaction", "list", params)



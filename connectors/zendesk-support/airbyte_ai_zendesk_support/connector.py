"""
zendesk-support connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    Article,
    ArticleAttachment,
    ArticleAttachmentsDownloadParams,
    ArticleAttachmentsGetParams,
    ArticleAttachmentsListParams,
    ArticleAttachmentsListResultMeta,
    ArticlesGetParams,
    ArticlesListParams,
    ArticlesListResultMeta,
    Attachment,
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    Automation,
    AutomationsGetParams,
    AutomationsListParams,
    AutomationsListResultMeta,
    Brand,
    BrandsGetParams,
    BrandsListParams,
    BrandsListResultMeta,
    Group,
    GroupMembership,
    GroupMembershipsListParams,
    GroupMembershipsListResultMeta,
    GroupsGetParams,
    GroupsListParams,
    GroupsListResultMeta,
    Macro,
    MacrosGetParams,
    MacrosListParams,
    MacrosListResultMeta,
    Organization,
    OrganizationMembership,
    OrganizationMembershipsListParams,
    OrganizationMembershipsListResultMeta,
    OrganizationsGetParams,
    OrganizationsListParams,
    OrganizationsListResultMeta,
    SLAPolicy,
    SatisfactionRating,
    SatisfactionRatingsGetParams,
    SatisfactionRatingsListParams,
    SatisfactionRatingsListResultMeta,
    SlaPoliciesGetParams,
    SlaPoliciesListParams,
    SlaPoliciesListResultMeta,
    Tag,
    TagsListParams,
    TagsListResultMeta,
    Ticket,
    TicketAudit,
    TicketAuditsListParams,
    TicketAuditsListResultMeta,
    TicketComment,
    TicketCommentsListParams,
    TicketCommentsListResultMeta,
    TicketField,
    TicketFieldsGetParams,
    TicketFieldsListParams,
    TicketFieldsListResultMeta,
    TicketForm,
    TicketFormsGetParams,
    TicketFormsListParams,
    TicketFormsListResultMeta,
    TicketMetric,
    TicketMetricsListParams,
    TicketMetricsListResultMeta,
    TicketsGetParams,
    TicketsListParams,
    TicketsListResultMeta,
    Trigger,
    TriggersGetParams,
    TriggersListParams,
    TriggersListResultMeta,
    User,
    UsersGetParams,
    UsersListParams,
    UsersListResultMeta,
    View,
    ViewsGetParams,
    ViewsListParams,
    ViewsListResultMeta,
)

if TYPE_CHECKING:
    from .models import ZendeskSupportAuthConfig

# Import envelope models at runtime (needed for instantiation in action methods)
from .models import (
    ZendeskSupportExecuteResult,
    ZendeskSupportExecuteResultWithMeta,
)


class ZendeskSupportConnector:
    """
    Type-safe Zendesk-Support API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-support"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("tickets", "list"): True,
        ("tickets", "get"): True,
        ("users", "list"): True,
        ("users", "get"): True,
        ("organizations", "list"): True,
        ("organizations", "get"): True,
        ("groups", "list"): True,
        ("groups", "get"): True,
        ("ticket_comments", "list"): True,
        ("attachments", "get"): True,
        ("attachments", "download"): False,
        ("ticket_audits", "list"): True,
        ("ticket_audits", "list"): True,
        ("ticket_metrics", "list"): True,
        ("ticket_fields", "list"): True,
        ("ticket_fields", "get"): True,
        ("brands", "list"): True,
        ("brands", "get"): True,
        ("views", "list"): True,
        ("views", "get"): True,
        ("macros", "list"): True,
        ("macros", "get"): True,
        ("triggers", "list"): True,
        ("triggers", "get"): True,
        ("automations", "list"): True,
        ("automations", "get"): True,
        ("tags", "list"): True,
        ("satisfaction_ratings", "list"): True,
        ("satisfaction_ratings", "get"): True,
        ("group_memberships", "list"): True,
        ("organization_memberships", "list"): True,
        ("sla_policies", "list"): True,
        ("sla_policies", "get"): True,
        ("ticket_forms", "list"): True,
        ("ticket_forms", "get"): True,
        ("articles", "list"): True,
        ("articles", "get"): True,
        ("article_attachments", "list"): True,
        ("article_attachments", "get"): True,
        ("article_attachments", "download"): False,
    }

    def __init__(
        self,
        auth_config: ZendeskSupportAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new zendesk-support connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Zendesk subdomain
        Examples:
            # Local mode (direct API calls)
            connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = ZendeskSupportConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = ZendeskSupportConnector(
                auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="..."),
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
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.tickets = TicketsQuery(self)
        self.users = UsersQuery(self)
        self.organizations = OrganizationsQuery(self)
        self.groups = GroupsQuery(self)
        self.ticket_comments = TicketCommentsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.ticket_audits = TicketAuditsQuery(self)
        self.ticket_metrics = TicketMetricsQuery(self)
        self.ticket_fields = TicketFieldsQuery(self)
        self.brands = BrandsQuery(self)
        self.views = ViewsQuery(self)
        self.macros = MacrosQuery(self)
        self.triggers = TriggersQuery(self)
        self.automations = AutomationsQuery(self)
        self.tags = TagsQuery(self)
        self.satisfaction_ratings = SatisfactionRatingsQuery(self)
        self.group_memberships = GroupMembershipsQuery(self)
        self.organization_memberships = OrganizationMembershipsQuery(self)
        self.sla_policies = SlaPoliciesQuery(self)
        self.ticket_forms = TicketFormsQuery(self)
        self.articles = ArticlesQuery(self)
        self.article_attachments = ArticleAttachmentsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["list"],
        params: "TicketsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["get"],
        params: "TicketsGetParams"
    ) -> "ZendeskSupportExecuteResult[Ticket]": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "ZendeskSupportExecuteResult[User]": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["list"],
        params: "OrganizationsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["get"],
        params: "OrganizationsGetParams"
    ) -> "ZendeskSupportExecuteResult[Organization]": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["list"],
        params: "GroupsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["get"],
        params: "GroupsGetParams"
    ) -> "ZendeskSupportExecuteResult[Group]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_comments"],
        action: Literal["list"],
        params: "TicketCommentsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams"
    ) -> "ZendeskSupportExecuteResult[Attachment]": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_audits"],
        action: Literal["list"],
        params: "TicketAuditsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_audits"],
        action: Literal["list"],
        params: "TicketAuditsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_metrics"],
        action: Literal["list"],
        params: "TicketMetricsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_fields"],
        action: Literal["list"],
        params: "TicketFieldsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_fields"],
        action: Literal["get"],
        params: "TicketFieldsGetParams"
    ) -> "ZendeskSupportExecuteResult[TicketField]": ...

    @overload
    async def execute(
        self,
        entity: Literal["brands"],
        action: Literal["list"],
        params: "BrandsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["brands"],
        action: Literal["get"],
        params: "BrandsGetParams"
    ) -> "ZendeskSupportExecuteResult[Brand]": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["list"],
        params: "ViewsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["get"],
        params: "ViewsGetParams"
    ) -> "ZendeskSupportExecuteResult[View]": ...

    @overload
    async def execute(
        self,
        entity: Literal["macros"],
        action: Literal["list"],
        params: "MacrosListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["macros"],
        action: Literal["get"],
        params: "MacrosGetParams"
    ) -> "ZendeskSupportExecuteResult[Macro]": ...

    @overload
    async def execute(
        self,
        entity: Literal["triggers"],
        action: Literal["list"],
        params: "TriggersListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["triggers"],
        action: Literal["get"],
        params: "TriggersGetParams"
    ) -> "ZendeskSupportExecuteResult[Trigger]": ...

    @overload
    async def execute(
        self,
        entity: Literal["automations"],
        action: Literal["list"],
        params: "AutomationsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["automations"],
        action: Literal["get"],
        params: "AutomationsGetParams"
    ) -> "ZendeskSupportExecuteResult[Automation]": ...

    @overload
    async def execute(
        self,
        entity: Literal["tags"],
        action: Literal["list"],
        params: "TagsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["satisfaction_ratings"],
        action: Literal["list"],
        params: "SatisfactionRatingsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["satisfaction_ratings"],
        action: Literal["get"],
        params: "SatisfactionRatingsGetParams"
    ) -> "ZendeskSupportExecuteResult[SatisfactionRating]": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_memberships"],
        action: Literal["list"],
        params: "GroupMembershipsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["organization_memberships"],
        action: Literal["list"],
        params: "OrganizationMembershipsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["sla_policies"],
        action: Literal["list"],
        params: "SlaPoliciesListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["sla_policies"],
        action: Literal["get"],
        params: "SlaPoliciesGetParams"
    ) -> "ZendeskSupportExecuteResult[SLAPolicy]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_forms"],
        action: Literal["list"],
        params: "TicketFormsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_forms"],
        action: Literal["get"],
        params: "TicketFormsGetParams"
    ) -> "ZendeskSupportExecuteResult[TicketForm]": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["list"],
        params: "ArticlesListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["get"],
        params: "ArticlesGetParams"
    ) -> "ZendeskSupportExecuteResult[Article]": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["list"],
        params: "ArticleAttachmentsListParams"
    ) -> "ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["get"],
        params: "ArticleAttachmentsGetParams"
    ) -> "ZendeskSupportExecuteResult[ArticleAttachment]": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["download"],
        params: "ArticleAttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> ZendeskSupportExecuteResult[Any] | ZendeskSupportExecuteResultWithMeta[Any, Any] | Any: ...

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
                return ZendeskSupportExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZendeskSupportExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class TicketsQuery:
    """
    Query class for Tickets entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        external_id: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]:
        """
        Returns a list of all tickets in your account

        Args:
            page: Page number for pagination
            external_id: Lists tickets by external id
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "external_id": external_id,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ticket_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Ticket]:
        """
        Returns a ticket by its ID

        Args:
            ticket_id: The ID of the ticket
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Ticket]
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Ticket](data=result.data)



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        role: str | None = None,
        external_id: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]:
        """
        Returns a list of all users in your account

        Args:
            page: Page number for pagination
            role: Filter by role
            external_id: Filter by external id
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "role": role,
            "external_id": external_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        user_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[User]:
        """
        Returns a user by their ID

        Args:
            user_id: The ID of the user
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[User]
        """
        params = {k: v for k, v in {
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[User](data=result.data)



class OrganizationsQuery:
    """
    Query class for Organizations entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]:
        """
        Returns a list of all organizations in your account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        organization_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Organization]:
        """
        Returns an organization by its ID

        Args:
            organization_id: The ID of the organization
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Organization]
        """
        params = {k: v for k, v in {
            "organization_id": organization_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Organization](data=result.data)



class GroupsQuery:
    """
    Query class for Groups entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        exclude_deleted: bool | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]:
        """
        Returns a list of all groups in your account

        Args:
            page: Page number for pagination
            exclude_deleted: Exclude deleted groups
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "exclude_deleted": exclude_deleted,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        group_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Group]:
        """
        Returns a group by its ID

        Args:
            group_id: The ID of the group
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Group]
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Group](data=result.data)



class TicketCommentsQuery:
    """
    Query class for TicketComments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ticket_id: str,
        page: int | None = None,
        include_inline_images: bool | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]:
        """
        Returns a list of comments for a specific ticket

        Args:
            ticket_id: The ID of the ticket
            page: Page number for pagination
            include_inline_images: Include inline images in the response
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            "page": page,
            "include_inline_images": include_inline_images,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_comments", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        attachment_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Attachment]:
        """
        Returns an attachment by its ID

        Args:
            attachment_id: The ID of the attachment
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Attachment]
        """
        params = {k: v for k, v in {
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Attachment](data=result.data)



    async def download(
        self,
        attachment_id: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the file content of a ticket attachment

        Args:
            attachment_id: The ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "attachment_id": attachment_id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_local(
        self,
        attachment_id: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the file content of a ticket attachment and save to file.

        Args:
            attachment_id: The ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            attachment_id=attachment_id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class TicketAuditsQuery:
    """
    Query class for TicketAudits entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]:
        """
        Returns a list of all ticket audits

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_audits", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def list(
        self,
        ticket_id: str,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]:
        """
        Returns a list of audits for a specific ticket

        Args:
            ticket_id: The ID of the ticket
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_audits", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class TicketMetricsQuery:
    """
    Query class for TicketMetrics entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]:
        """
        Returns a list of all ticket metrics

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_metrics", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class TicketFieldsQuery:
    """
    Query class for TicketFields entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        locale: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]:
        """
        Returns a list of all ticket fields

        Args:
            page: Page number for pagination
            locale: Locale for the results
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "locale": locale,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ticket_field_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[TicketField]:
        """
        Returns a ticket field by its ID

        Args:
            ticket_field_id: The ID of the ticket field
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[TicketField]
        """
        params = {k: v for k, v in {
            "ticket_field_id": ticket_field_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[TicketField](data=result.data)



class BrandsQuery:
    """
    Query class for Brands entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]:
        """
        Returns a list of all brands for the account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("brands", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        brand_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Brand]:
        """
        Returns a brand by its ID

        Args:
            brand_id: The ID of the brand
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Brand]
        """
        params = {k: v for k, v in {
            "brand_id": brand_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("brands", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Brand](data=result.data)



class ViewsQuery:
    """
    Query class for Views entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        access: str | None = None,
        active: bool | None = None,
        group_id: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]:
        """
        Returns a list of all views for the account

        Args:
            page: Page number for pagination
            access: Filter by access level
            active: Filter by active status
            group_id: Filter by group ID
            sort_by: Sort results
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "access": access,
            "active": active,
            "group_id": group_id,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        view_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[View]:
        """
        Returns a view by its ID

        Args:
            view_id: The ID of the view
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[View]
        """
        params = {k: v for k, v in {
            "view_id": view_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[View](data=result.data)



class MacrosQuery:
    """
    Query class for Macros entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        access: str | None = None,
        active: bool | None = None,
        category: int | None = None,
        group_id: int | None = None,
        only_viewable: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]:
        """
        Returns a list of all macros for the account

        Args:
            page: Page number for pagination
            access: Filter by access level
            active: Filter by active status
            category: Filter by category
            group_id: Filter by group ID
            only_viewable: Return only viewable macros
            sort_by: Sort results
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "access": access,
            "active": active,
            "category": category,
            "group_id": group_id,
            "only_viewable": only_viewable,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("macros", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        macro_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Macro]:
        """
        Returns a macro by its ID

        Args:
            macro_id: The ID of the macro
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Macro]
        """
        params = {k: v for k, v in {
            "macro_id": macro_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("macros", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Macro](data=result.data)



class TriggersQuery:
    """
    Query class for Triggers entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        category_id: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]:
        """
        Returns a list of all triggers for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            category_id: Filter by category ID
            sort: Sort results
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "category_id": category_id,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        trigger_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Trigger]:
        """
        Returns a trigger by its ID

        Args:
            trigger_id: The ID of the trigger
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Trigger]
        """
        params = {k: v for k, v in {
            "trigger_id": trigger_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Trigger](data=result.data)



class AutomationsQuery:
    """
    Query class for Automations entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]:
        """
        Returns a list of all automations for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            sort: Sort results
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        automation_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Automation]:
        """
        Returns an automation by its ID

        Args:
            automation_id: The ID of the automation
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Automation]
        """
        params = {k: v for k, v in {
            "automation_id": automation_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Automation](data=result.data)



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]:
        """
        Returns a list of all tags used in the account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class SatisfactionRatingsQuery:
    """
    Query class for SatisfactionRatings entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        score: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]:
        """
        Returns a list of all satisfaction ratings

        Args:
            page: Page number for pagination
            score: Filter by score
            start_time: Start time (Unix epoch)
            end_time: End time (Unix epoch)
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "score": score,
            "start_time": start_time,
            "end_time": end_time,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        satisfaction_rating_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[SatisfactionRating]:
        """
        Returns a satisfaction rating by its ID

        Args:
            satisfaction_rating_id: The ID of the satisfaction rating
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[SatisfactionRating]
        """
        params = {k: v for k, v in {
            "satisfaction_rating_id": satisfaction_rating_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[SatisfactionRating](data=result.data)



class GroupMembershipsQuery:
    """
    Query class for GroupMemberships entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]:
        """
        Returns a list of all group memberships

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_memberships", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class OrganizationMembershipsQuery:
    """
    Query class for OrganizationMemberships entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]:
        """
        Returns a list of all organization memberships

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organization_memberships", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta](
            data=result.data,
            meta=result.meta
        )



class SlaPoliciesQuery:
    """
    Query class for SlaPolicies entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]:
        """
        Returns a list of all SLA policies

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sla_policies", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        sla_policy_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[SLAPolicy]:
        """
        Returns an SLA policy by its ID

        Args:
            sla_policy_id: The ID of the SLA policy
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[SLAPolicy]
        """
        params = {k: v for k, v in {
            "sla_policy_id": sla_policy_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sla_policies", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[SLAPolicy](data=result.data)



class TicketFormsQuery:
    """
    Query class for TicketForms entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        end_user_visible: bool | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]:
        """
        Returns a list of all ticket forms for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            end_user_visible: Filter by end user visibility
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "end_user_visible": end_user_visible,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ticket_form_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[TicketForm]:
        """
        Returns a ticket form by its ID

        Args:
            ticket_form_id: The ID of the ticket form
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[TicketForm]
        """
        params = {k: v for k, v in {
            "ticket_form_id": ticket_form_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[TicketForm](data=result.data)



class ArticlesQuery:
    """
    Query class for Articles entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]:
        """
        Returns a list of all articles in the Help Center

        Args:
            page: Page number for pagination
            sort_by: Sort articles by field
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]
        """
        params = {k: v for k, v in {
            "page": page,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResult[Article]:
        """
        Retrieves the details of a specific article

        Args:
            id: The unique ID of the article
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[Article]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[Article](data=result.data)



class ArticleAttachmentsQuery:
    """
    Query class for ArticleAttachments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        article_id: str,
        page: int | None = None,
        **kwargs
    ) -> ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]:
        """
        Returns a list of all attachments for a specific article

        Args:
            article_id: The unique ID of the article
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "list", params)
        # Cast generic envelope to typed envelope with proper data/meta types
        return ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta](
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        article_id: str,
        attachment_id: str,
        **kwargs
    ) -> ZendeskSupportExecuteResult[ArticleAttachment]:
        """
        Retrieves the metadata of a specific attachment for a specific article

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            **kwargs: Additional parameters

        Returns:
            ZendeskSupportExecuteResult[ArticleAttachment]
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "get", params)
        # Cast generic envelope to typed envelope with proper data type
        return ZendeskSupportExecuteResult[ArticleAttachment](data=result.data)



    async def download(
        self,
        article_id: str,
        attachment_id: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the file content of a specific attachment

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "attachment_id": attachment_id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "download", params)
        return result


    async def download_local(
        self,
        article_id: str,
        attachment_id: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the file content of a specific attachment and save to file.

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            article_id=article_id,
            attachment_id=attachment_id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


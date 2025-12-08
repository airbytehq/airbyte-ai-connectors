"""
Pydantic models for zendesk-support connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic
from typing import Optional

# Import types needed for result type aliases
from .types import (
    Article,
    ArticleAttachment,
    ArticleAttachmentsListResultMeta,
    ArticlesListResultMeta,
    Attachment,
    Automation,
    AutomationsListResultMeta,
    Brand,
    BrandsListResultMeta,
    Group,
    GroupMembership,
    GroupMembershipsListResultMeta,
    GroupsListResultMeta,
    Macro,
    MacrosListResultMeta,
    Organization,
    OrganizationMembership,
    OrganizationMembershipsListResultMeta,
    OrganizationsListResultMeta,
    SLAPolicy,
    SatisfactionRating,
    SatisfactionRatingsListResultMeta,
    SlaPoliciesListResultMeta,
    Tag,
    TagsListResultMeta,
    Ticket,
    TicketAudit,
    TicketAuditsListResultMeta,
    TicketComment,
    TicketCommentsListResultMeta,
    TicketField,
    TicketFieldsListResultMeta,
    TicketForm,
    TicketFormsListResultMeta,
    TicketMetric,
    TicketMetricsListResultMeta,
    TicketsListResultMeta,
    Trigger,
    TriggersListResultMeta,
    User,
    UsersListResultMeta,
    View,
    ViewsListResultMeta,
)

# Authentication configuration

class ZendeskSupportAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """OAuth2 access token"""
    refresh_token: Optional[str] = None
    """OAuth2 refresh token (optional)"""
    client_id: Optional[str] = None
    """OAuth2 client ID (optional)"""
    client_secret: Optional[str] = None
    """OAuth2 client secret (optional)"""

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class ZendeskSupportExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class ZendeskSupportExecuteResultWithMeta(ZendeskSupportExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TicketsListResult = ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

TicketsGetResult = ZendeskSupportExecuteResult[Ticket]
"""Result type for tickets.get operation."""

UsersListResult = ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersGetResult = ZendeskSupportExecuteResult[User]
"""Result type for users.get operation."""

OrganizationsListResult = ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]
"""Result type for organizations.list operation with data and metadata."""

OrganizationsGetResult = ZendeskSupportExecuteResult[Organization]
"""Result type for organizations.get operation."""

GroupsListResult = ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]
"""Result type for groups.list operation with data and metadata."""

GroupsGetResult = ZendeskSupportExecuteResult[Group]
"""Result type for groups.get operation."""

TicketCommentsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]
"""Result type for ticket_comments.list operation with data and metadata."""

AttachmentsGetResult = ZendeskSupportExecuteResult[Attachment]
"""Result type for attachments.get operation."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketMetricsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]
"""Result type for ticket_metrics.list operation with data and metadata."""

TicketFieldsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]
"""Result type for ticket_fields.list operation with data and metadata."""

TicketFieldsGetResult = ZendeskSupportExecuteResult[TicketField]
"""Result type for ticket_fields.get operation."""

BrandsListResult = ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]
"""Result type for brands.list operation with data and metadata."""

BrandsGetResult = ZendeskSupportExecuteResult[Brand]
"""Result type for brands.get operation."""

ViewsListResult = ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]
"""Result type for views.list operation with data and metadata."""

ViewsGetResult = ZendeskSupportExecuteResult[View]
"""Result type for views.get operation."""

MacrosListResult = ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]
"""Result type for macros.list operation with data and metadata."""

MacrosGetResult = ZendeskSupportExecuteResult[Macro]
"""Result type for macros.get operation."""

TriggersListResult = ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]
"""Result type for triggers.list operation with data and metadata."""

TriggersGetResult = ZendeskSupportExecuteResult[Trigger]
"""Result type for triggers.get operation."""

AutomationsListResult = ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]
"""Result type for automations.list operation with data and metadata."""

AutomationsGetResult = ZendeskSupportExecuteResult[Automation]
"""Result type for automations.get operation."""

TagsListResult = ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

SatisfactionRatingsListResult = ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]
"""Result type for satisfaction_ratings.list operation with data and metadata."""

SatisfactionRatingsGetResult = ZendeskSupportExecuteResult[SatisfactionRating]
"""Result type for satisfaction_ratings.get operation."""

GroupMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]
"""Result type for group_memberships.list operation with data and metadata."""

OrganizationMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]
"""Result type for organization_memberships.list operation with data and metadata."""

SlaPoliciesListResult = ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]
"""Result type for sla_policies.list operation with data and metadata."""

SlaPoliciesGetResult = ZendeskSupportExecuteResult[SLAPolicy]
"""Result type for sla_policies.get operation."""

TicketFormsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]
"""Result type for ticket_forms.list operation with data and metadata."""

TicketFormsGetResult = ZendeskSupportExecuteResult[TicketForm]
"""Result type for ticket_forms.get operation."""

ArticlesListResult = ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]
"""Result type for articles.list operation with data and metadata."""

ArticlesGetResult = ZendeskSupportExecuteResult[Article]
"""Result type for articles.get operation."""

ArticleAttachmentsListResult = ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]
"""Result type for article_attachments.list operation with data and metadata."""

ArticleAttachmentsGetResult = ZendeskSupportExecuteResult[ArticleAttachment]
"""Result type for article_attachments.get operation."""


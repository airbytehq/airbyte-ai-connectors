"""
Type definitions for zendesk-support connector.
"""
# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any

# ===== RESPONSE TYPE DEFINITIONS =====

class Ticket(TypedDict):
    """Zendesk Support ticket object"""
    id: int
    url: NotRequired[str]
    external_id: NotRequired[str | None]
    type: NotRequired[str | None]
    subject: NotRequired[str]
    raw_subject: NotRequired[str]
    description: NotRequired[str]
    priority: NotRequired[str | None]
    status: NotRequired[str]
    recipient: NotRequired[str | None]
    requester_id: NotRequired[int]
    submitter_id: NotRequired[int]
    assignee_id: NotRequired[int | None]
    organization_id: NotRequired[int | None]
    group_id: NotRequired[int | None]
    collaborator_ids: NotRequired[list[int]]
    follower_ids: NotRequired[list[int]]
    email_cc_ids: NotRequired[list[int]]
    forum_topic_id: NotRequired[int | None]
    problem_id: NotRequired[int | None]
    has_incidents: NotRequired[bool]
    is_public: NotRequired[bool]
    due_at: NotRequired[str | None]
    tags: NotRequired[list[str]]
    custom_fields: NotRequired[list[dict[str, Any]]]
    satisfaction_rating: NotRequired[dict[str, Any]]
    sharing_agreement_ids: NotRequired[list[int]]
    custom_status_id: NotRequired[int]
    fields: NotRequired[list[dict[str, Any]]]
    followup_ids: NotRequired[list[int]]
    ticket_form_id: NotRequired[int]
    brand_id: NotRequired[int]
    allow_channelback: NotRequired[bool]
    allow_attachments: NotRequired[bool]
    from_messaging_channel: NotRequired[bool]
    generated_timestamp: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    via: NotRequired[dict[str, Any]]

class User(TypedDict):
    """Zendesk Support user object"""
    id: int
    url: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[str | None]
    alias: NotRequired[str | None]
    phone: NotRequired[str | None]
    time_zone: NotRequired[str]
    locale: NotRequired[str]
    locale_id: NotRequired[int]
    organization_id: NotRequired[int | None]
    role: NotRequired[str]
    role_type: NotRequired[int | None]
    custom_role_id: NotRequired[int | None]
    external_id: NotRequired[str | None]
    tags: NotRequired[list[str]]
    active: NotRequired[bool]
    verified: NotRequired[bool]
    shared: NotRequired[bool]
    shared_agent: NotRequired[bool]
    shared_phone_number: NotRequired[bool | None]
    signature: NotRequired[str | None]
    details: NotRequired[str | None]
    notes: NotRequired[str | None]
    suspended: NotRequired[bool]
    restricted_agent: NotRequired[bool]
    only_private_comments: NotRequired[bool]
    moderator: NotRequired[bool]
    ticket_restriction: NotRequired[str | None]
    default_group_id: NotRequired[int | None]
    report_csv: NotRequired[bool]
    photo: NotRequired[dict[str, Any] | None]
    user_fields: NotRequired[dict[str, Any]]
    last_login_at: NotRequired[str | None]
    two_factor_auth_enabled: NotRequired[bool | None]
    iana_time_zone: NotRequired[str]
    permanently_deleted: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Organization(TypedDict):
    """Zendesk Support organization object"""
    id: int
    url: NotRequired[str]
    name: NotRequired[str]
    details: NotRequired[str | None]
    notes: NotRequired[str | None]
    group_id: NotRequired[int | None]
    shared_tickets: NotRequired[bool]
    shared_comments: NotRequired[bool]
    external_id: NotRequired[str | None]
    domain_names: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    organization_fields: NotRequired[dict[str, Any]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Group(TypedDict):
    """Zendesk Support group object"""
    id: int
    url: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    default: NotRequired[bool]
    deleted: NotRequired[bool]
    is_public: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class TicketComment(TypedDict):
    """Zendesk Support ticket comment object"""
    id: int
    type: NotRequired[str]
    body: NotRequired[str]
    html_body: NotRequired[str]
    plain_body: NotRequired[str]
    public: NotRequired[bool]
    author_id: NotRequired[int]
    attachments: NotRequired[list[dict[str, Any]]]
    audit_id: NotRequired[int]
    via: NotRequired[dict[str, Any]]
    metadata: NotRequired[dict[str, Any]]
    created_at: NotRequired[str]

class Attachment(TypedDict):
    """Zendesk Support attachment object"""
    id: int
    file_name: NotRequired[str]
    content_url: NotRequired[str]
    mapped_content_url: NotRequired[str]
    content_type: NotRequired[str]
    size: NotRequired[int]
    width: NotRequired[int | None]
    height: NotRequired[int | None]
    inline: NotRequired[bool]
    deleted: NotRequired[bool]
    malware_access_override: NotRequired[bool]
    malware_scan_result: NotRequired[str]
    url: NotRequired[str]
    thumbnails: NotRequired[list[dict[str, Any]]]

class TicketAudit(TypedDict):
    """Zendesk Support ticket audit object"""
    id: int
    ticket_id: NotRequired[int]
    author_id: NotRequired[int]
    metadata: NotRequired[dict[str, Any]]
    via: NotRequired[dict[str, Any]]
    events: NotRequired[list[dict[str, Any]]]
    created_at: NotRequired[str]

class TicketMetric(TypedDict):
    """Zendesk Support ticket metric object"""
    id: int
    url: NotRequired[str]
    ticket_id: NotRequired[int]
    group_stations: NotRequired[int]
    assignee_stations: NotRequired[int]
    reopens: NotRequired[int]
    replies: NotRequired[int]
    assignee_updated_at: NotRequired[str | None]
    requester_updated_at: NotRequired[str]
    status_updated_at: NotRequired[str]
    initially_assigned_at: NotRequired[str | None]
    assigned_at: NotRequired[str | None]
    solved_at: NotRequired[str | None]
    latest_comment_added_at: NotRequired[str]
    reply_time_in_minutes: NotRequired[dict[str, Any]]
    first_resolution_time_in_minutes: NotRequired[dict[str, Any]]
    full_resolution_time_in_minutes: NotRequired[dict[str, Any]]
    agent_wait_time_in_minutes: NotRequired[dict[str, Any]]
    requester_wait_time_in_minutes: NotRequired[dict[str, Any]]
    on_hold_time_in_minutes: NotRequired[dict[str, Any]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class TicketField(TypedDict):
    """Zendesk Support ticket field object"""
    id: int
    url: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    raw_title: NotRequired[str]
    description: NotRequired[str]
    raw_description: NotRequired[str]
    position: NotRequired[int]
    active: NotRequired[bool]
    required: NotRequired[bool]
    collapsed_for_agents: NotRequired[bool]
    regexp_for_validation: NotRequired[str | None]
    title_in_portal: NotRequired[str]
    raw_title_in_portal: NotRequired[str]
    visible_in_portal: NotRequired[bool]
    editable_in_portal: NotRequired[bool]
    required_in_portal: NotRequired[bool]
    tag: NotRequired[str | None]
    custom_field_options: NotRequired[list[dict[str, Any]]]
    system_field_options: NotRequired[list[dict[str, Any]]]
    sub_type_id: NotRequired[int]
    removable: NotRequired[bool]
    agent_description: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Brand(TypedDict):
    """Zendesk Support brand object"""
    id: int
    url: NotRequired[str]
    name: NotRequired[str]
    brand_url: NotRequired[str]
    subdomain: NotRequired[str]
    host_mapping: NotRequired[str | None]
    has_help_center: NotRequired[bool]
    help_center_state: NotRequired[str]
    active: NotRequired[bool]
    default: NotRequired[bool]
    is_deleted: NotRequired[bool]
    logo: NotRequired[dict[str, Any] | None]
    ticket_form_ids: NotRequired[list[int]]
    signature_template: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class View(TypedDict):
    """Zendesk Support view object"""
    id: int
    url: NotRequired[str]
    title: NotRequired[str]
    active: NotRequired[bool]
    position: NotRequired[int]
    description: NotRequired[str | None]
    execution: NotRequired[dict[str, Any]]
    conditions: NotRequired[dict[str, Any]]
    restriction: NotRequired[dict[str, Any] | None]
    raw_title: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Macro(TypedDict):
    """Zendesk Support macro object"""
    id: int
    url: NotRequired[str]
    title: NotRequired[str]
    active: NotRequired[bool]
    position: NotRequired[int]
    description: NotRequired[str]
    actions: NotRequired[list[dict[str, Any]]]
    restriction: NotRequired[dict[str, Any] | None]
    raw_title: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Trigger(TypedDict):
    """Zendesk Support trigger object"""
    id: int
    url: NotRequired[str]
    title: NotRequired[str]
    active: NotRequired[bool]
    position: NotRequired[int]
    description: NotRequired[str | None]
    conditions: NotRequired[dict[str, Any]]
    actions: NotRequired[list[dict[str, Any]]]
    raw_title: NotRequired[str]
    category_id: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Automation(TypedDict):
    """Zendesk Support automation object"""
    id: int
    url: NotRequired[str]
    title: NotRequired[str]
    active: NotRequired[bool]
    position: NotRequired[int]
    conditions: NotRequired[dict[str, Any]]
    actions: NotRequired[list[dict[str, Any]]]
    raw_title: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Tag(TypedDict):
    """Zendesk Support tag object"""
    name: str
    count: NotRequired[int]

class SatisfactionRating(TypedDict):
    """Zendesk Support satisfaction rating object"""
    id: int
    url: NotRequired[str]
    assignee_id: NotRequired[int | None]
    group_id: NotRequired[int | None]
    requester_id: NotRequired[int]
    ticket_id: NotRequired[int]
    score: NotRequired[str]
    comment: NotRequired[str | None]
    reason: NotRequired[str | None]
    reason_id: NotRequired[int | None]
    reason_code: NotRequired[int | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class GroupMembership(TypedDict):
    """Zendesk Support group membership object"""
    id: int
    url: NotRequired[str]
    user_id: NotRequired[int]
    group_id: NotRequired[int]
    default: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class OrganizationMembership(TypedDict):
    """Zendesk Support organization membership object"""
    id: int
    url: NotRequired[str]
    user_id: NotRequired[int]
    organization_id: NotRequired[int]
    default: NotRequired[bool]
    organization_name: NotRequired[str]
    view_tickets: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class SLAPolicy(TypedDict):
    """Zendesk Support SLA policy object"""
    id: int
    url: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    position: NotRequired[int]
    filter: NotRequired[dict[str, Any]]
    policy_metrics: NotRequired[list[dict[str, Any]]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class TicketForm(TypedDict):
    """Zendesk Support ticket form object"""
    id: int
    url: NotRequired[str]
    name: NotRequired[str]
    display_name: NotRequired[str]
    raw_name: NotRequired[str]
    raw_display_name: NotRequired[str]
    position: NotRequired[int]
    active: NotRequired[bool]
    end_user_visible: NotRequired[bool]
    default: NotRequired[bool]
    in_all_brands: NotRequired[bool]
    restricted_brand_ids: NotRequired[list[int]]
    ticket_field_ids: NotRequired[list[int]]
    agent_conditions: NotRequired[list[dict[str, Any]]]
    end_user_conditions: NotRequired[list[dict[str, Any]]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class Article(TypedDict):
    """Help Center article object"""
    id: int
    url: NotRequired[str]
    html_url: NotRequired[str]
    title: NotRequired[str]
    body: NotRequired[str]
    locale: NotRequired[str]
    author_id: NotRequired[int]
    section_id: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    vote_sum: NotRequired[int]
    vote_count: NotRequired[int]
    label_names: NotRequired[list[str]]
    draft: NotRequired[bool]
    promoted: NotRequired[bool]
    position: NotRequired[int]

class ArticleAttachment(TypedDict):
    """Article attachment object"""
    id: int
    url: NotRequired[str]
    article_id: NotRequired[int]
    file_name: str
    content_type: NotRequired[str]
    content_url: NotRequired[str]
    size: NotRequired[int]
    inline: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

# ===== METADATA TYPE DEFINITIONS =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TicketsListResultMeta(TypedDict):
    """Metadata for tickets.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class UsersListResultMeta(TypedDict):
    """Metadata for users.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class OrganizationsListResultMeta(TypedDict):
    """Metadata for organizations.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class GroupsListResultMeta(TypedDict):
    """Metadata for groups.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TicketCommentsListResultMeta(TypedDict):
    """Metadata for ticket_comments.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TicketAuditsListResultMeta(TypedDict):
    """Metadata for ticket_audits.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TicketMetricsListResultMeta(TypedDict):
    """Metadata for ticket_metrics.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TicketFieldsListResultMeta(TypedDict):
    """Metadata for ticket_fields.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class BrandsListResultMeta(TypedDict):
    """Metadata for brands.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class ViewsListResultMeta(TypedDict):
    """Metadata for views.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class MacrosListResultMeta(TypedDict):
    """Metadata for macros.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TriggersListResultMeta(TypedDict):
    """Metadata for triggers.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class AutomationsListResultMeta(TypedDict):
    """Metadata for automations.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TagsListResultMeta(TypedDict):
    """Metadata for tags.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class SatisfactionRatingsListResultMeta(TypedDict):
    """Metadata for satisfaction_ratings.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class GroupMembershipsListResultMeta(TypedDict):
    """Metadata for group_memberships.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class OrganizationMembershipsListResultMeta(TypedDict):
    """Metadata for organization_memberships.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class SlaPoliciesListResultMeta(TypedDict):
    """Metadata for sla_policies.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class TicketFormsListResultMeta(TypedDict):
    """Metadata for ticket_forms.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class ArticlesListResultMeta(TypedDict):
    """Metadata for articles.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

class ArticleAttachmentsListResultMeta(TypedDict):
    """Metadata for article_attachments.list operation"""
    next_page: Any
    previous_page: Any
    count: Any

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    page: NotRequired[int]
    external_id: NotRequired[str]
    sort: NotRequired[str]

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    page: NotRequired[int]
    role: NotRequired[str]
    external_id: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_id: str

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    page: NotRequired[int]

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    organization_id: str

class GroupsListParams(TypedDict):
    """Parameters for groups.list operation"""
    page: NotRequired[int]
    exclude_deleted: NotRequired[bool]

class GroupsGetParams(TypedDict):
    """Parameters for groups.get operation"""
    group_id: str

class TicketCommentsListParams(TypedDict):
    """Parameters for ticket_comments.list operation"""
    ticket_id: str
    page: NotRequired[int]
    include_inline_images: NotRequired[bool]
    sort: NotRequired[str]

class AttachmentsGetParams(TypedDict):
    """Parameters for attachments.get operation"""
    attachment_id: str

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    attachment_id: str
    range_header: NotRequired[str]

class TicketAuditsListParams(TypedDict):
    """Parameters for ticket_audits.list operation"""
    page: NotRequired[int]

class TicketAuditsListParams(TypedDict):
    """Parameters for ticket_audits.list operation"""
    ticket_id: str
    page: NotRequired[int]

class TicketMetricsListParams(TypedDict):
    """Parameters for ticket_metrics.list operation"""
    page: NotRequired[int]

class TicketFieldsListParams(TypedDict):
    """Parameters for ticket_fields.list operation"""
    page: NotRequired[int]
    locale: NotRequired[str]

class TicketFieldsGetParams(TypedDict):
    """Parameters for ticket_fields.get operation"""
    ticket_field_id: str

class BrandsListParams(TypedDict):
    """Parameters for brands.list operation"""
    page: NotRequired[int]

class BrandsGetParams(TypedDict):
    """Parameters for brands.get operation"""
    brand_id: str

class ViewsListParams(TypedDict):
    """Parameters for views.list operation"""
    page: NotRequired[int]
    access: NotRequired[str]
    active: NotRequired[bool]
    group_id: NotRequired[int]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ViewsGetParams(TypedDict):
    """Parameters for views.get operation"""
    view_id: str

class MacrosListParams(TypedDict):
    """Parameters for macros.list operation"""
    page: NotRequired[int]
    access: NotRequired[str]
    active: NotRequired[bool]
    category: NotRequired[int]
    group_id: NotRequired[int]
    only_viewable: NotRequired[bool]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class MacrosGetParams(TypedDict):
    """Parameters for macros.get operation"""
    macro_id: str

class TriggersListParams(TypedDict):
    """Parameters for triggers.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    category_id: NotRequired[str]
    sort: NotRequired[str]

class TriggersGetParams(TypedDict):
    """Parameters for triggers.get operation"""
    trigger_id: str

class AutomationsListParams(TypedDict):
    """Parameters for automations.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    sort: NotRequired[str]

class AutomationsGetParams(TypedDict):
    """Parameters for automations.get operation"""
    automation_id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    page: NotRequired[int]

class SatisfactionRatingsListParams(TypedDict):
    """Parameters for satisfaction_ratings.list operation"""
    page: NotRequired[int]
    score: NotRequired[str]
    start_time: NotRequired[int]
    end_time: NotRequired[int]

class SatisfactionRatingsGetParams(TypedDict):
    """Parameters for satisfaction_ratings.get operation"""
    satisfaction_rating_id: str

class GroupMembershipsListParams(TypedDict):
    """Parameters for group_memberships.list operation"""
    page: NotRequired[int]

class OrganizationMembershipsListParams(TypedDict):
    """Parameters for organization_memberships.list operation"""
    page: NotRequired[int]

class SlaPoliciesListParams(TypedDict):
    """Parameters for sla_policies.list operation"""
    page: NotRequired[int]

class SlaPoliciesGetParams(TypedDict):
    """Parameters for sla_policies.get operation"""
    sla_policy_id: str

class TicketFormsListParams(TypedDict):
    """Parameters for ticket_forms.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    end_user_visible: NotRequired[bool]

class TicketFormsGetParams(TypedDict):
    """Parameters for ticket_forms.get operation"""
    ticket_form_id: str

class ArticlesListParams(TypedDict):
    """Parameters for articles.list operation"""
    page: NotRequired[int]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ArticlesGetParams(TypedDict):
    """Parameters for articles.get operation"""
    id: str

class ArticleAttachmentsListParams(TypedDict):
    """Parameters for article_attachments.list operation"""
    article_id: str
    page: NotRequired[int]

class ArticleAttachmentsGetParams(TypedDict):
    """Parameters for article_attachments.get operation"""
    article_id: str
    attachment_id: str

class ArticleAttachmentsDownloadParams(TypedDict):
    """Parameters for article_attachments.download operation"""
    article_id: str
    attachment_id: str
    range_header: NotRequired[str]

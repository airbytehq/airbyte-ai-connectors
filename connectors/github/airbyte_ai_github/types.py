"""
Auto-generated type definitions for github connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class GithubAuthConfig(TypedDict):
    """Authentication"""
    access_token: str  # OAuth2 access token
    refresh_token: NotRequired[str]  # OAuth2 refresh token (optional)
    client_id: NotRequired[str]  # OAuth2 client ID (optional)
    client_secret: NotRequired[str]  # OAuth2 client secret (optional)

# ===== RESPONSE TYPE DEFINITIONS =====

class Repository(TypedDict):
    """GitHub repository object"""
    id: int
    node_id: str
    name: str
    full_name: str
    owner: dict[str, Any]
    private: bool
    html_url: str
    description: NotRequired[str | None]
    fork: bool
    url: NotRequired[str]
    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    forks_url: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    git_url: NotRequired[str]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    notifications_url: NotRequired[str]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    ssh_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    clone_url: NotRequired[str]
    mirror_url: NotRequired[str | None]
    hooks_url: NotRequired[str]
    svn_url: NotRequired[str]
    homepage: NotRequired[str | None]
    language: NotRequired[str | None]
    forks_count: NotRequired[int]
    forks: NotRequired[int]
    stargazers_count: NotRequired[int]
    watchers_count: NotRequired[int]
    watchers: NotRequired[int]
    size: NotRequired[int]
    default_branch: NotRequired[str]
    open_issues_count: NotRequired[int]
    open_issues: NotRequired[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    has_pages: NotRequired[bool]
    has_downloads: NotRequired[bool]
    has_discussions: NotRequired[bool]
    archived: NotRequired[bool]
    disabled: NotRequired[bool]
    visibility: NotRequired[str]
    pushed_at: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    permissions: NotRequired[dict[str, Any]]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    license: NotRequired[dict[str, Any] | None]
    parent: NotRequired[dict[str, Any] | None]
    source: NotRequired[dict[str, Any] | None]
    template_repository: NotRequired[dict[str, Any] | None]
    organization: NotRequired[dict[str, Any] | None]
    security_and_analysis: NotRequired[dict[str, Any] | None]
    temp_clone_token: NotRequired[str | None]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class RepositoriesGetParams(TypedDict):
    """Parameters for repositories.get operation"""
    owner: str
    repo: str
    fields: NotRequired[list[str]]

class RepositoriesListParams(TypedDict):
    """Parameters for repositories.list operation"""
    username: str
    per_page: NotRequired[int]
    fields: NotRequired[list[str]]

class RepositoriesSearchParams(TypedDict):
    """Parameters for repositories.search operation"""
    query: str
    limit: NotRequired[int]
    fields: NotRequired[list[str]]

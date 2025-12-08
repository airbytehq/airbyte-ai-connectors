# Airbyte Zendesk-Support AI Connector

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.18.0

**Connector Version:** 0.1.1

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-zendesk-support
```

## Usage

```python
from airbyte_ai_zendesk_support import ZendeskSupportConnector
from airbyte_ai_zendesk_support.models import ZendeskSupportAuthConfig

# Create connector
connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Tickets Operations
- `list_tickets()` - Returns a list of all tickets in your account
- `get_ticket()` - Returns a ticket by its ID

### Users Operations
- `list_users()` - Returns a list of all users in your account
- `get_user()` - Returns a user by their ID

### Organizations Operations
- `list_organizations()` - Returns a list of all organizations in your account
- `get_organization()` - Returns an organization by its ID

### Groups Operations
- `list_groups()` - Returns a list of all groups in your account
- `get_group()` - Returns a group by its ID

### Ticket_Comments Operations
- `list_ticket_comments()` - Returns a list of comments for a specific ticket

### Attachments Operations
- `get_attachment()` - Returns an attachment by its ID
- `download_attachment()` - Downloads the file content of a ticket attachment

### Ticket_Audits Operations
- `list_ticket_audits()` - Returns a list of all ticket audits
- `list_audits_for_ticket()` - Returns a list of audits for a specific ticket

### Ticket_Metrics Operations
- `list_ticket_metrics()` - Returns a list of all ticket metrics

### Ticket_Fields Operations
- `list_ticket_fields()` - Returns a list of all ticket fields
- `get_ticket_field()` - Returns a ticket field by its ID

### Brands Operations
- `list_brands()` - Returns a list of all brands for the account
- `get_brand()` - Returns a brand by its ID

### Views Operations
- `list_views()` - Returns a list of all views for the account
- `get_view()` - Returns a view by its ID

### Macros Operations
- `list_macros()` - Returns a list of all macros for the account
- `get_macro()` - Returns a macro by its ID

### Triggers Operations
- `list_triggers()` - Returns a list of all triggers for the account
- `get_trigger()` - Returns a trigger by its ID

### Automations Operations
- `list_automations()` - Returns a list of all automations for the account
- `get_automation()` - Returns an automation by its ID

### Tags Operations
- `list_tags()` - Returns a list of all tags used in the account

### Satisfaction_Ratings Operations
- `list_satisfaction_ratings()` - Returns a list of all satisfaction ratings
- `get_satisfaction_rating()` - Returns a satisfaction rating by its ID

### Group_Memberships Operations
- `list_group_memberships()` - Returns a list of all group memberships

### Organization_Memberships Operations
- `list_organization_memberships()` - Returns a list of all organization memberships

### Sla_Policies Operations
- `list_sla_policies()` - Returns a list of all SLA policies
- `get_sla_policy()` - Returns an SLA policy by its ID

### Ticket_Forms Operations
- `list_ticket_forms()` - Returns a list of all ticket forms for the account
- `get_ticket_form()` - Returns a ticket form by its ID

### Articles Operations
- `list_articles()` - Returns a list of all articles in the Help Center
- `get_article()` - Retrieves the details of a specific article

### Article_Attachments Operations
- `list_article_attachments()` - Returns a list of all attachments for a specific article
- `get_article_attachment_metadata()` - Retrieves the metadata of a specific attachment for a specific article
- `download_article_attachment()` - Downloads the file content of a specific attachment

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_zendesk_support.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.

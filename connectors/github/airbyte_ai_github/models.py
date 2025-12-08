"""
Pydantic models for github connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic
from typing import Optional


# Authentication configuration

class GithubAuthConfig(BaseModel):
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


class GithubExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class GithubExecuteResultWithMeta(GithubExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.


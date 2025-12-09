"""Data models for connector-mcp configuration and responses."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class BackoffType(str, Enum):
    """Retry backoff strategy."""

    EXPONENTIAL = "exponential"
    LINEAR = "linear"


class ErrorType(str, Enum):
    """Categorized error types for retry logic."""

    RATE_LIMIT = "rate_limit"
    TIMEOUT = "timeout"
    SERVER_ERROR = "server_error"
    UNKNOWN = "unknown"


class ConnectorType(str, Enum):
    """Type of connector."""

    LOCAL = "local"
    HOSTED = "hosted"


class ConnectorConfig(BaseModel):
    """Configuration for a single connector."""

    id: str = Field(..., description="Unique connector identifier")
    type: ConnectorType = Field(..., description="Connector type")
    path: str | None = Field(None, description="Path to connector.yaml (local only)")
    description: str = Field(default="", description="Human-readable description")
    secrets: dict[str, str] = Field(default_factory=dict, description="Mapping of secret param names to secret keys")

    def model_post_init(self, __context):
        """Validate connector-type-specific fields."""
        if self.type == ConnectorType.LOCAL and not self.path:
            raise ValueError(f"LOCAL connector '{self.id}' must specify 'path'")


class Config(BaseModel):
    """Root configuration model."""

    connectors: list[ConnectorConfig] = Field(..., min_length=1)

    def get_connector(self, connector_id: str) -> ConnectorConfig:
        """Look up connector by ID."""
        for connector in self.connectors:
            if connector.id == connector_id:
                return connector
        raise ValueError(f"Connector not found: {connector_id}")


class ExecuteResponse(BaseModel):
    """Response from execute tool."""

    success: bool
    data: Any = None
    error: dict | None = None
    connector_id: str
    entity: str
    action: str


class EntityInfo(BaseModel):
    """Information about a connector entity."""

    name: str
    description: str = ""
    available_actions: list[str]


class ListEntitiesResponse(BaseModel):
    """Response from list_entities tool."""

    connector_id: str
    entities: list[EntityInfo]


class DescribeEntityResponse(BaseModel):
    """Response from describe_entity tool."""

    connector_id: str
    entity: str
    actions: dict
    schema: dict


class ValidationError(BaseModel):
    """Validation error detail."""

    field: str
    message: str


class ValidateOperationResponse(BaseModel):
    """Response from validate_operation tool."""

    valid: bool
    errors: list[ValidationError] = Field(default_factory=list)


class ConnectorInfo(BaseModel):
    """Information about a configured connector."""

    id: str = Field(..., description="Connector identifier")
    type: str = Field(..., description="Connector type (local or remote)")
    description: str = Field(default="", description="Human-readable description")


class DiscoverConnectorsResponse(BaseModel):
    """Response from discover_connectors tool."""

    connectors: list[ConnectorInfo] = Field(..., description="List of configured connectors")

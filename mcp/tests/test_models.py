"""Test data models."""

import pytest
from pydantic import ValidationError

from connector_mcp.models import (
    ConnectorConfig,
    ConnectorType,
)


def test_local_connector_requires_path():
    """Test LOCAL connector validation."""
    with pytest.raises(ValidationError):
        ConnectorConfig(
            id="test",
            type=ConnectorType.LOCAL,
            # Missing path!
        )


def test_hosted_connector_valid():
    """Test HOSTED connector validation."""
    # HOSTED connectors don't require path
    connector = ConnectorConfig(id="test", type=ConnectorType.HOSTED, description="Test hosted connector")
    assert connector.id == "test"
    assert connector.type == ConnectorType.HOSTED

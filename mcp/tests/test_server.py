"""Test MCP server tools."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from airbyte_agent_mcp.config import load_connector_config
from airbyte_agent_mcp.connector_manager import ConnectorManager
from airbyte_agent_mcp.secret_manager import SecretsManager


@pytest.fixture
def setup_server():
    """Set up server with test configuration."""
    # Create a test configuration
    config_content = """
connectors:
  - id: test_local
    type: local
    path: /tmp/test_connector.yaml
    description: "Test local connector"
    secrets:
      api_key: TEST_KEY
  - id: test_hosted
    type: hosted
    description: "Test hosted connector"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        # Load config and set up server
        config = load_connector_config(config_path)

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)

        # Create connector manager
        connector_manager = ConnectorManager(config, secrets_manager)

        yield connector_manager

    finally:
        Path(config_path).unlink()


@pytest.mark.asyncio
async def test_discover_connectors(setup_server):
    """Test discover_connectors tool returns all configured connectors."""
    result = setup_server.discover_connectors()

    assert "connectors" in result
    assert len(result["connectors"]) == 2

    # Check first connector (local)
    local_connector = result["connectors"][0]
    assert local_connector["id"] == "test_local"
    assert local_connector["type"] == "local"
    assert local_connector["description"] == "Test local connector"

    # Check second connector (hosted)
    hosted_connector = result["connectors"][1]
    assert hosted_connector["id"] == "test_hosted"
    assert hosted_connector["type"] == "hosted"
    assert hosted_connector["description"] == "Test hosted connector"


@pytest.mark.asyncio
async def test_discover_connectors_single():
    """Test discover_connectors with single connector configured."""
    # Set up config with single connector
    config_content = """
connectors:
  - id: single
    type: local
    path: /tmp/test.yaml
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_connector_config(config_path)
        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        connector_manager = ConnectorManager(config, secrets_manager)

        result = connector_manager.discover_connectors()

        assert "connectors" in result
        assert len(result["connectors"]) == 1
        assert result["connectors"][0]["id"] == "single"

    finally:
        Path(config_path).unlink()

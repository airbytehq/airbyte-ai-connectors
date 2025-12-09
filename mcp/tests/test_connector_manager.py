"""Test connector manager."""

import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from connector_mcp._vendored.connector_sdk.executor.models import ExecutionConfig

from connector_mcp.connector_manager import ConnectorManager
from connector_mcp.models import Config, ConnectorConfig, ConnectorType
from connector_mcp.secret_manager import SecretsManager


@pytest.fixture
def mock_secrets_manager():
    """Create a mock secrets manager."""
    backend = MagicMock()
    backend.get_secret.return_value = "test_secret_value"
    return SecretsManager(backend)


@pytest.fixture
def simple_config():
    """Create a simple test configuration."""
    return Config(
        connectors=[
            ConnectorConfig(
                id="test_yaml",
                type=ConnectorType.LOCAL,
                path="/tmp/test_connector.yaml",
                secrets={"token": "TEST_KEY"},
            )
        ]
    )


@pytest.mark.asyncio
async def test_execute_connector_not_found(mock_secrets_manager, simple_config):
    """Test error when connector not found."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    with pytest.raises(ValueError, match="Connector not found: nonexistent"):
        await manager.execute(connector_id="nonexistent", entity="customers", action="list")


@pytest.mark.asyncio
async def test_execute_success(mock_secrets_manager, simple_config):
    """Test successful execution of a connector operation."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value={"data": [{"id": "cust_123", "email": "test@example.com"}]})

    with patch("connector_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        result = await manager.execute(connector_id="test_yaml", entity="customers", action="list", params={"limit": 10})

        assert result == {"data": [{"id": "cust_123", "email": "test@example.com"}]}
        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={"limit": 10}))


@pytest.mark.asyncio
async def test_execute_with_secrets(simple_config):
    """Test that secrets are resolved and passed to connector."""
    backend = MagicMock()
    backend.get_secret.return_value = "secret_api_key_value"
    secrets_manager = SecretsManager(backend)

    manager = ConnectorManager(simple_config, secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value={"success": True})

    with patch("connector_mcp.connector_manager.ConnectorExecutor") as MockConnectorExecutor:
        MockConnectorExecutor.return_value = mock_connector

        await manager.execute(connector_id="test_yaml", entity="customers", action="list")

        MockConnectorExecutor.assert_called_once_with(
            config_path="/tmp/test_connector.yaml", auth_config={"token": "secret_api_key_value"}, execution_context="mcp"
        )

        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={}))


@pytest.mark.asyncio
async def test_execute_without_params(mock_secrets_manager, simple_config):
    """Test execution with no params defaults to empty dict."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value={"data": []})

    with patch("connector_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        await manager.execute(connector_id="test_yaml", entity="customers", action="list")

        # Verify execute was called with empty dict
        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={}))


@pytest.mark.asyncio
async def test_describe_connector():
    # Create a test connector.yaml with complete OpenAPI spec
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/widgets:
    get:
      summary: List all widgets
      description: Returns a list of widgets
      operationId: widgets_List
      x-airbyte-entity: widgets
      x-airbyte-action: list
      tags:
        - Widgets
      parameters:
        - name: limit
          in: query
          description: A limit on the number of objects to be returned
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
      responses:
        "200":
          description: Success
          content:
            application/json:
              schema:
                type: object
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        assert entities[0]["name"] == "/v1/widgets"
        assert entities[0]["entity_name"] == "widgets"
        assert entities[0]["available_actions"] == ["list"]
        assert entities[0]["description"] == "Returns a list of widgets"

    finally:
        Path(yaml_path).unlink()

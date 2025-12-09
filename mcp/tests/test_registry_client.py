"""Tests for registry client."""

from unittest.mock import AsyncMock, patch

import pytest

from airbyte_agent_mcp.registry_client import REGISTRY_BASE_URL, RegistryClient


@pytest.fixture
def mock_registry_response():
    """Sample registry.json response."""
    return {
        "connectors": [
            {
                "connector_id": "stripe-uuid",
                "connector_name": "stripe",
                "latest_version": "2.0.0",
                "latest_url": f"{REGISTRY_BASE_URL}/definitions/stripe/2.0.0/connector.yaml",
                "versions": [
                    {
                        "version": "2.0.0",
                        "url": f"{REGISTRY_BASE_URL}/definitions/stripe/2.0.0/connector.yaml",
                    },
                    {
                        "version": "1.0.0",
                        "url": f"{REGISTRY_BASE_URL}/definitions/stripe/1.0.0/connector.yaml",
                    },
                ],
            },
            {
                "connector_id": "salesforce-uuid",
                "connector_name": "salesforce",
                "latest_version": "1.5.0",
                "latest_url": f"{REGISTRY_BASE_URL}/definitions/salesforce/1.5.0/connector.yaml",
                "versions": [
                    {
                        "version": "1.5.0",
                        "url": f"{REGISTRY_BASE_URL}/definitions/salesforce/1.5.0/connector.yaml",
                    },
                ],
            },
        ],
        "last_updated": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def registry_client():
    """Create a registry client."""
    return RegistryClient()


@pytest.mark.asyncio
async def test_resolve_connector_url_latest(registry_client, mock_registry_response):
    """Test resolving connector URL to latest version."""
    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        url = await registry_client.resolve_connector_url("stripe")

        assert url == f"{REGISTRY_BASE_URL}/definitions/stripe/2.0.0/connector.yaml"


@pytest.mark.asyncio
async def test_resolve_connector_url_specific_version(registry_client, mock_registry_response):
    """Test resolving connector URL to specific version."""
    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        url = await registry_client.resolve_connector_url("stripe", version="1.0.0")

        assert url == f"{REGISTRY_BASE_URL}/definitions/stripe/1.0.0/connector.yaml"


@pytest.mark.asyncio
async def test_resolve_connector_url_not_found(registry_client, mock_registry_response):
    """Test error when connector not found."""
    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        with pytest.raises(ValueError, match="Connector not found in registry: unknown"):
            await registry_client.resolve_connector_url("unknown")


@pytest.mark.asyncio
async def test_resolve_connector_url_version_not_found(registry_client, mock_registry_response):
    """Test error when version not found."""
    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        with pytest.raises(ValueError, match="Version 99.0.0 not found for stripe"):
            await registry_client.resolve_connector_url("stripe", version="99.0.0")


@pytest.mark.asyncio
async def test_download_connector(registry_client, mock_registry_response):
    """Test downloading connector.yaml."""
    connector_yaml_content = "openapi: 3.1.0\ninfo:\n  title: Stripe\n"

    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        # Mock the actual HTTP download
        with patch("airbyte_agent_mcp.registry_client.httpx.AsyncClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client

            mock_response = AsyncMock()
            mock_response.text = connector_yaml_content
            mock_response.raise_for_status = lambda: None
            mock_client.get.return_value = mock_response

            path = await registry_client.download_connector("stripe")

            assert path.exists()
            assert path.read_text() == connector_yaml_content
            assert "stripe" in str(path)
            assert "2.0.0" in str(path)


@pytest.mark.asyncio
async def test_download_connector_with_version(registry_client, mock_registry_response):
    """Test downloading specific version of connector.yaml."""
    connector_yaml_content = "openapi: 3.1.0\ninfo:\n  title: Stripe v1.0.0\n"

    with patch.object(registry_client, "fetch_registry", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_registry_response

        # Mock the actual HTTP download
        with patch("airbyte_agent_mcp.registry_client.httpx.AsyncClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client

            mock_response = AsyncMock()
            mock_response.text = connector_yaml_content
            mock_response.raise_for_status = lambda: None
            mock_client.get.return_value = mock_response

            path = await registry_client.download_connector("stripe", version="1.0.0")

            assert path.exists()
            assert "stripe" in str(path)
            assert "1.0.0" in str(path)

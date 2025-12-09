"""Client for fetching connectors from the Airbyte registry."""

import atexit
import logging
import shutil
import tempfile
from pathlib import Path
from typing import Any

import httpx

logger = logging.getLogger(__name__)

REGISTRY_BASE_URL = "https://connectors.airbyte.ai"
REGISTRY_JSON_URL = f"{REGISTRY_BASE_URL}/registry.json"


class RegistryClient:
    """Client for the Airbyte connector registry.

    Downloads connectors fresh from registry on each use (no caching).
    Uses temp directory for downloaded connector.yaml files.
    """

    def __init__(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="airbyte-connectors-"))
        atexit.register(self._cleanup)

    def _cleanup(self):
        """Clean up temp directory on exit."""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    async def fetch_registry(self) -> dict[str, Any]:
        """Fetch the registry.json index (always fresh)."""
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(REGISTRY_JSON_URL)
            response.raise_for_status()
            return response.json()

    async def resolve_connector_url(
        self,
        connector_name: str,
        version: str | None = None,
    ) -> str:
        """Resolve connector to a download URL.

        Args:
            connector_name: Connector name (e.g., "stripe")
            version: Specific version or None for latest

        Returns:
            URL to download connector.yaml
        """
        registry = await self.fetch_registry()

        # Find connector by name
        connector = None
        for c in registry["connectors"]:
            if c["connector_name"] == connector_name:
                connector = c
                break

        if not connector:
            raise ValueError(f"Connector not found in registry: {connector_name}")

        # Get version URL
        if version:
            for v in connector["versions"]:
                if v["version"] == version:
                    return v["url"]
            raise ValueError(f"Version {version} not found for {connector['connector_name']}")

        return connector["latest_url"]

    async def download_connector(
        self,
        connector_name: str,
        version: str | None = None,
    ) -> Path:
        """Download connector.yaml and return path (cached within session)."""
        url = await self.resolve_connector_url(connector_name, version)

        # Create temp path based on URL
        parts = url.replace(f"{REGISTRY_BASE_URL}/definitions/", "").split("/")
        name, ver = parts[0], parts[1]
        temp_path = self.temp_dir / name / ver / "connector.yaml"

        # Return cached version if already downloaded
        if temp_path.exists():
            logger.debug(f"Using cached connector: {temp_path}")
            return temp_path

        # Download fresh
        logger.info(f"Downloading connector from: {url}")
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url)
            response.raise_for_status()

            temp_path.parent.mkdir(parents=True, exist_ok=True)
            temp_path.write_text(response.text)

        return temp_path

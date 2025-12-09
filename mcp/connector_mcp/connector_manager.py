"""Connector instantiation and execution management."""

import logging
from typing import Any

from ._vendored.connector_sdk import LocalExecutor as ConnectorExecutor
from ._vendored.connector_sdk.config_loader import load_connector_config
from ._vendored.connector_sdk.executor.models import ExecutionConfig

from connector_mcp.models import Config, ConnectorInfo, ConnectorType, DiscoverConnectorsResponse
from connector_mcp.secret_manager import SecretsManager

logger = logging.getLogger(__name__)


class ConnectorManager:
    """Manages connector lifecycle and execution."""

    def __init__(self, config: Config, secrets_manager: SecretsManager):
        """Initialize manager.

        Args:
            config: Configuration with connector definitions
            secrets_manager: Secrets manager for resolving credentials
        """
        self.config = config
        self.secrets_manager = secrets_manager

    async def execute(
        self,
        connector_id: str,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute an operation on a connector.

        This is stateless - creates a fresh connector instance for each call.

        Args:
            connector_id: Connector ID from config
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "list", "get", "create")
            params: Operation parameters (optional)

        Returns:
            Result from connector execution

        Raises:
            ValueError: If connector not found
            Exception: Any error from connector execution
        """
        params = params or {}

        logger.info(f"Executing: {connector_id}.{entity}.{action} with params: {list(params.keys())}")

        connector_config = self.config.get_connector(connector_id)

        secrets = {}
        if connector_config.secrets:
            secrets = self.secrets_manager.get_secrets(connector_config.secrets)
            logger.debug(f"Resolved {len(secrets)} secret(s)")

        connector = self._create_yaml_connector(connector_config.path, secrets)

        logger.debug(f"Calling connector.execute({entity}, {action}, ...)")
        result = await connector.execute(ExecutionConfig(entity=entity, action=action, params=params))

        logger.info("Execution successful")
        return result

    def _create_yaml_connector(self, path: str, secrets: dict[str, Any]) -> Any:
        """Create a YAML-based connector instance.

        Args:
            path: Path to connector.yaml file
            secrets: Resolved secrets dict

        Returns:
            ConnectorExecutor instance
        """
        logger.debug(f"Creating YAML connector from: {path}")
        connector = ConnectorExecutor(config_path=path, auth_config=secrets, execution_context="mcp")

        return connector

    async def describe_connector(self, connector_id: str) -> list[dict[str, Any]]:
        """List available entities for a connector.

        Args:
            connector_id: Connector ID from config

        Returns:
            List of entity info dicts
        """
        logger.info(f"Listing entities for: {connector_id}")

        connector_config = self.config.get_connector(connector_id)
        if connector_config.type == ConnectorType.LOCAL:
            return await self._describe_connector_from_sdk(connector_config.path)

    async def _describe_connector_from_sdk(self, path: str) -> list[dict[str, Any]]:
        """List entities from a YAML connector definition.

        Args:
            path: Path to connector.yaml (OpenAPI spec)

        Returns:
            List of entity info dicts
        """

        # Load and parse the connector config using SDK
        connector_config = load_connector_config(path)

        entities = []
        for entity_def in connector_config.entities:
            # Get the first endpoint to extract path and description
            # (all endpoints for an entity typically share the same base path)
            first_endpoint = None
            description = ""
            path_name = ""

            if entity_def.endpoints:
                # Get first endpoint from the dict
                first_endpoint = next(iter(entity_def.endpoints.values()))
                path_name = first_endpoint.path
                description = first_endpoint.description or ""

            # Convert Action enums to strings
            available_actions = [action.value for action in entity_def.actions]

            entities.append(
                {
                    "name": path_name,
                    "entity_name": entity_def.name,
                    "description": description,
                    "available_actions": available_actions,
                }
            )

        return entities

    def discover_connectors(self) -> dict[str, Any]:
        """Discover all available configured connectors.

        Returns:
            Dictionary with list of connector information
        """
        logger.info("Discovering connectors from configuration")

        # Build list of connector info
        connector_infos = [
            ConnectorInfo(
                id=connector.id,
                type=connector.type.value,  # Convert enum to string
                description=connector.description,
            )
            for connector in self.config.connectors
        ]

        response = DiscoverConnectorsResponse(connectors=connector_infos)

        return response.model_dump()

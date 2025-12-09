"""Test configuration loading."""

import tempfile
from pathlib import Path

import pytest

from airbyte_agent_mcp.config import load_connector_config, validate_connectors
from airbyte_agent_mcp.models import Config, ConnectorConfig, ConnectorType


def test_load_config_file_not_found():
    """Test error when config file doesn't exist."""
    with pytest.raises(FileNotFoundError, match="Configuration file not found"):
        load_connector_config("nonexistent.yaml")


def test_load_config_empty_file():
    """Test error when config file is empty."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write("")
        config_path = f.name

    try:
        with pytest.raises(ValueError, match="Configuration file is empty"):
            load_connector_config(config_path)
    finally:
        Path(config_path).unlink()


def test_load_config_valid():
    """Test loading valid configuration."""
    config_content = """
connectors:
  - id: test_connector
    type: local
    path: test_package
    description: Test connector
    secrets:
      api_key: TEST_KEY
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_connector_config(config_path)

        assert len(config.connectors) == 1
        assert config.connectors[0].id == "test_connector"
    finally:
        Path(config_path).unlink()


def test_load_config_with_defaults():
    """Test loading config uses defaults for optional fields."""
    config_content = """
connectors:
  - id: minimal
    type: local
    path: test_package
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_connector_config(config_path)

        assert config.connectors[0].secrets == {}
    finally:
        Path(config_path).unlink()


def test_validate_connectors_local_missing_file():
    """Test validation fails for missing LOCAL connector file."""
    config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path="/nonexistent/connector.yaml")])

    errors = validate_connectors(config)

    assert len(errors) == 1
    assert "File not found" in errors[0]


def test_validate_connectors_local_existing_file():
    """Test validation succeeds for existing LOCAL connector file."""
    # Create a temporary connector.yaml
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write("connector:\n  name: test\n")
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        errors = validate_connectors(config)
        assert len(errors) == 0
    finally:
        Path(yaml_path).unlink()

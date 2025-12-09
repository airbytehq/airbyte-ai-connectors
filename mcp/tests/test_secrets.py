"""Test secrets management."""

import os
import tempfile

import pytest

from airbyte_agent_mcp.secret_manager import (
    DotEnvSecretsBackend,
    SecretsManager,
)


def test_dotenv_backend_from_environment():
    """Test loading secrets from environment variables."""
    # Set a test environment variable
    os.environ["TEST_SECRET"] = "test_value"

    backend = DotEnvSecretsBackend(dotenv_path="nonexistent.env")
    value = backend.get_secret("TEST_SECRET")

    assert value == "test_value"

    # Clean up
    del os.environ["TEST_SECRET"]


def test_dotenv_backend_from_file():
    """Test loading secrets from .env file."""
    # Create a temporary .env file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
        f.write("TEST_SECRET=from_file\n")
        env_path = f.name

    try:
        backend = DotEnvSecretsBackend(dotenv_path=env_path)
        value = backend.get_secret("TEST_SECRET")
        assert value == "from_file"
    finally:
        os.unlink(env_path)


def test_dotenv_backend_caching():
    """Test that secrets are cached."""
    os.environ["TEST_SECRET"] = "cached_value"

    backend = DotEnvSecretsBackend()

    # First call
    value1 = backend.get_secret("TEST_SECRET")

    # Change environment (shouldn't affect cached value)
    os.environ["TEST_SECRET"] = "new_value"

    # Second call should return cached value
    value2 = backend.get_secret("TEST_SECRET")

    assert value1 == value2 == "cached_value"

    # Clean up
    del os.environ["TEST_SECRET"]


def test_dotenv_backend_not_found():
    """Test handling of missing secrets."""
    backend = DotEnvSecretsBackend()
    value = backend.get_secret("NONEXISTENT_SECRET")
    assert value is None


def test_secrets_manager_resolve():
    """Test secrets manager resolution."""
    os.environ["KEY1"] = "value1"
    os.environ["KEY2"] = "value2"

    backend = DotEnvSecretsBackend()
    manager = SecretsManager(backend)

    secrets = manager.get_secrets({"api_key": "KEY1", "token": "KEY2"})

    assert secrets == {"api_key": "value1", "token": "value2"}

    # Clean up
    del os.environ["KEY1"]
    del os.environ["KEY2"]


def test_secrets_manager_missing_secret():
    """Test error on missing secret."""
    backend = DotEnvSecretsBackend()
    manager = SecretsManager(backend)

    with pytest.raises(ValueError, match="Required secrets not found: MISSING"):
        manager.get_secrets({"api_key": "MISSING"})

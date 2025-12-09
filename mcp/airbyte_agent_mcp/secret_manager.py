"""Secrets management with pluggable backends."""

import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv


class SecretsBackend(ABC):
    """Abstract base class for secrets backends."""

    @abstractmethod
    def get_secret(self, key: str) -> str | None:
        """Get a secret value by key."""
        pass


class DotEnvSecretsBackend(SecretsBackend):
    """Secrets backend that loads from .env file and environment variables."""

    def __init__(self, dotenv_path: str = ".env"):
        """Initialize backend.

        Args:
            dotenv_path: Path to .env file (default: ".env" in current directory)
        """
        self.dotenv_path = dotenv_path
        self._cache: dict[str, str] = {}

        # Load .env file if it exists
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path, override=True)

    def get_secret(self, key: str) -> str | None:
        """Get secret from cache, then environment.

        Args:
            key: Secret key to look up

        Returns:
            Secret value or None if not found
        """
        # Check cache first
        if key in self._cache:
            return self._cache[key]

        # Try environment variable
        value = os.getenv(key)
        if value is not None:
            self._cache[key] = value
            return value

        return None


class SecretsManager:
    """Facade for managing secrets resolution."""

    def __init__(self, backend: SecretsBackend):
        """Initialize manager with a backend.

        Args:
            backend: Secrets backend implementation
        """
        self.backend = backend

    def get_secrets(self, secret_mapping: dict[str, str]) -> dict[str, str]:
        """Resolve multiple secrets from a mapping.

        Args:
            secret_mapping: Dict mapping param names to secret keys
                Example: {"api_key": "STRIPE_API_KEY"}

        Returns:
            Dict mapping param names to secret values
                Example: {"api_key": "sk_test_abc123"}

        Raises:
            ValueError: If any secret is not found
        """
        resolved = {}
        missing = []

        for param_name, secret_key in secret_mapping.items():
            value = self.backend.get_secret(secret_key)
            if value is None:
                missing.append(secret_key)
            else:
                resolved[param_name] = value

        if missing:
            raise ValueError(f"Required secrets not found: {', '.join(missing)}. Check your .env file or environment variables.")

        return resolved

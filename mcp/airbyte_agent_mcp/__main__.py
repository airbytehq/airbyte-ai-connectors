"""Entry point for running airbyte-agent-mcp server."""

import sys

from airbyte_agent_mcp.server import run_server


def main():
    """Main entry point."""
    # Support optional command-line arguments
    config_path = "configured_connectors.yaml"
    dotenv_path = ".env"

    # Simple argument parsing
    args = sys.argv[1:]
    if len(args) >= 1:
        config_path = args[0]
    if len(args) >= 2:
        dotenv_path = args[1]

    # Run the server
    run_server(config_path, dotenv_path)


if __name__ == "__main__":
    main()

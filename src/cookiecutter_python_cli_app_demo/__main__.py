"""cookiecutter-python-cli-app-demo as a module entry point.

This allows cookiecutter-python-cli-app-demo to be executable from a git checkout or zip archive.
"""

from .cli import cli

if __name__ == "__main__":
    cli()

# CLI Reference

This page lists the `--help` for `cookiecutter-python-cli-app-demo`.

## cookiecutter-python-cli-app-demo

Running `cookiecutter-python-cli-app-demo --help` or `python -m cookiecutter_python_cli_app_demo --help` shows a list of all of the available options and arguments:

<!-- [[[cog
import cog
from click.testing import CliRunner
from cookiecutter_python_cli_app_demo import cli
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
output = result.output.replace("Usage: cli", "Usage: cookiecutter-python-cli-app-demo")
help_text = "\n".join(line.rstrip() for line in output.splitlines()).rstrip()
cog.outl(f"\n```shell\ncookiecutter-python-cli-app-demo --help\n{help_text}\n```\n")
]]] -->
<!-- [[[end]]] -->

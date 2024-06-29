"""Main CLI for cookiecutter-python-cli-app-demo."""

import click

from . import __version__


@click.command(
    context_settings={"help_option_names": ["-h", "--help"], "show_default": True}
)
@click.argument("input_", metavar="INPUT")
@click.option(
    "-r",
    "--reverse",
    is_flag=True,
    help="Reverse the input.",
)
@click.version_option(__version__, "-v", "--version")
def cli(input_: str, *, reverse: bool = False) -> None:
    """Repeat the input.

    Demo of https://github.com/sgraaf/cookiecutter-python-cli-app.
    """
    click.echo(input_ if not reverse else input_[::-1])

"""Main CLI for cookiecutter-python-cli-app-demo."""
import click

from . import __version__


@click.group()
@click.version_option(__version__)
def cli() -> None:
    """Demo of https://github.com/sgraaf/cookiecutter-python-cli-app."""


@cli.command()
@click.argument("input_", metavar="INPUT")
@click.option(
    "-r",
    "--reverse",
    is_flag=True,
    help="Reverse the input.",
)
def repeat(input_: str, *, reverse: bool = False) -> None:
    """Repeat the input."""
    click.echo(input_ if not reverse else input_[::-1])

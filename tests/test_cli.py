from importlib import import_module
from importlib.metadata import version

import pytest
from click.testing import CliRunner

from cookiecutter_python_cli_app_demo.cli import cli

from .utils import run_command_in_shell


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_main_module() -> None:
    """Exercise (most of) the code in the `__main__` module."""
    import_module("cookiecutter_python_cli_app_demo.__main__")


def test_run_as_module() -> None:
    """Is the script runnable as a Python module?"""
    result = run_command_in_shell("python -m cookiecutter_python_cli_app_demo --help")
    assert result.exit_code == 0


def test_run_as_executable() -> None:
    """Is the script installed (as a `console_script`) and runnable as an executable?"""
    result = run_command_in_shell("cookiecutter-python-cli-app-demo --help")
    assert result.exit_code == 0


def test_version_runner(runner: CliRunner) -> None:
    """Does `--version` display the correct version?"""
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert (
        result.output == f"cli, version {version('cookiecutter-python-cli-app-demo')}\n"
    )

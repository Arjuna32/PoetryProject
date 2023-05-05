""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib


def test_check_empty_call(): # pragma
    runner = CliRunner()
    result = runner.invoke(_main.cli,["check"])
    assert result.exit_code == 0
    assert "Long form checking" in result.output

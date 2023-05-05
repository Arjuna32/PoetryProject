""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib


def test_check_empty_call2(): # pragma
    runner = CliRunner()
    result = runner.invoke(_main.cli,["check","--quick"])
#    assert "xx" in result.output
    assert result.exit_code == 0
    assert "Quick form checking" in result.output

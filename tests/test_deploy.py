""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib


def test_deploy_empty_call():
    runner = CliRunner()
    result = runner.invoke( _main.cli,["deploy"] )
    assert result.exit_code == 0


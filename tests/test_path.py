""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib


def test_path_empty_call():
    importlib.reload( _main )
    runner = CliRunner()
    result = runner.invoke( _main.cli,["path"] )
    assert result.exit_code == 0


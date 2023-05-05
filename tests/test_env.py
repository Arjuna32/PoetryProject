""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib



def test_env_empty_call():
    importlib.reload( _main )
    runner = CliRunner()
    result = runner.invoke( _main.cli,["env"] )
    assert result.exit_code == 0



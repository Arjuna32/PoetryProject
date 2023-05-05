""" docstring for tests """
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib

def test_build_empty_call():
    runner = CliRunner()
    result = runner.invoke( _main.cli,["build"] )
    #assert "xx"==result.output
    assert result.exit_code == 0

def test_build_help():
    runner = CliRunner()
    result = runner.invoke( _main.cli,["build",'--help'] )
    #assert "xx"==result.output
    assert result.exit_code == 0

def test_build_help3():
    runner = CliRunner()
    result = runner.invoke( _main.cli,["build","--docker"] )
    # assert "xx"==result.output
    assert result.exit_code == 0

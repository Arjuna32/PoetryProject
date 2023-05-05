""" docstring for tests """
import os
import subprocess
from click.testing import CliRunner
from bigcli import _main
import importlib


def test_empty_call():
    runner = CliRunner()
    result = runner.invoke(_main.cli)
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_help_output():
    runner = CliRunner()
    result = runner.invoke(_main.cli,["--help"])
    assert result.exit_code == 0

def test_version_output():
    runner = CliRunner()
    result = runner.invoke(_main.cli,["--version"])
    assert result.exit_code == 0

def test_config_file_absolute():
    runner = CliRunner()
    config_file = os.path.join(os.getcwd(), "pycli.toml")
    print(f"{config_file}")
    result = runner.invoke(_main.cli,["--log-level","TRACE","--config-file",f"{config_file}","--version"],"check")
    assert result.exit_code == 0

def test_config_file_relative():
    runner = CliRunner()
    config_file = os.path.join(".", "pycli.toml")
    print(f"{config_file}")
    result = runner.invoke(_main.cli,["--log-level","TRACE","--config-file",f"{config_file}","--version"],"check")
    assert result.exit_code == 0

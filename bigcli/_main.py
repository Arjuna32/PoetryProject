""" main.py docstring
"""
import os
import importlib.metadata

import click
from loguru import logger

from bigcli import click_config_file
from bigcli import DEFAULT_LOG_LEVEL
from bigcli import program_name
##from src.version import __version__

logger.trace(f"After imports {__file__}")

source_folder = os.path.dirname( __file__ )
plugin_folder = os.path.dirname(__file__)
logger.trace(f"source folder: {source_folder}")
logger.trace(f"plugin folder: {plugin_folder}")

# might be handy to open/close the DB before/after the group
#  https://click.palletsprojects.com/en/8.1.x/advanced/#managing-resources

class MyCLI(click.MultiCommand):
    """ CLI class """
    def list_commands(self, ctx): # pragma: no cover
        """ list_commands """
        logger.trace("list_commands")
        commands = []
        for filename in os.listdir(source_folder):
            if filename.startswith("cli_") and filename.endswith('.py') and filename != '__init__.py' and filename != "_main.py":
                commands.append(filename[4:-3])
        commands.sort()
        logger.trace(commands)
        return commands

    def get_command(self, ctx, cmd_name):
        """ get_command """
        filename = os.path.join(source_folder, "cli_" + cmd_name + '.py')
        namespace = {}
        namespace["__file__"] = filename
        try:
            with open(filename,'r',encoding='utf-8') as fhandle:
                logger.trace(f"running: {filename}")
                code = compile(fhandle.read(), filename, 'exec')
                eval(code, namespace, namespace) # pylint: disable=eval-used
            return namespace['cli']
        except IOError: # pragma: no cover
            logger.debug(f"Missing command: {cmd_name}")
        return None # pragma: no cover

def show_version():
    """ pull program name from __init__ and version from version.py """
    try:
        __version__ = importlib.metadata.version( "cmsc475-202320-final" )
    except ImportError: # pragma: no cover
        __version__ = "0.0.0"
    return f"{program_name} {__version__}" # pragma: no cover

@click.command(cls=MyCLI,help="tools subcommands loaded",invoke_without_command=True)
#@click.group(help=program_name+" - send commands to database",invoke_without_command=True)
@click.option('--log-level',
    default=DEFAULT_LOG_LEVEL,
    type=click.Choice(['TRACE','DEBUG','INFO','SUCCESS','WARNING','ERROR','CRITICAL'],
    case_sensitive=False)
)
@click.option('--config-file',type=click.Path(exists=True),help="path to config file")
@click.option('--version',"-v",is_flag=True,help="Print version number")
@click_config_file.configuration_option()
@click.pass_context
def cli(ctx,log_level,config_file,version): # pylint: disable=unused-argument
    """ main cli """
    if ctx.invoked_subcommand is None:
        if version :
            logger.info("version flag present")
            click.echo( show_version() )
        else:
            logger.info("No command provided. Invoking help.")
            click.echo( ctx.get_help() )
    else:
        logger.debug(f"Invoking (from main): {ctx.invoked_subcommand}")


#cli.add_command(build.build)
#cli.add_command(deploy.deploy)
#cli.add_command(check)

if __name__ == '__main__':
    cli() # pylint: disable=no-value-for-parameter # pragma: no cover

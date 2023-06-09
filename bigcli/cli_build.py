''' DOCSTRING for build.py
'''
import click
from loguru import logger
from bigcli import click_config_file,myprovider

logger.trace(f"After imports {__file__}")

@click.command()
@click.option('--docker', is_flag=True,
    help='Indicates the project should be built into docker image')
#@click_config_file.configuration_option()
@click_config_file.configuration_option(implicit=True,provider=myprovider)
def cli(docker):
    """ Command build docstring"""
    logger.info("Entering command build")
    if docker:
        print('Building this repo into a docker image...')
    else:
        print('Building this repo using default method...')

if __name__ == '__main__':
    cli() # pylint: disable=no-value-for-parameter # pragma: no cover

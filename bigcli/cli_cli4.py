""" module verify.py
"""
import os
import click
from loguru import logger
from bigcli import click_config_file,myprovider
import random
import string

logger.trace(f"After imports {__file__}")

@click.command()
#@click_config_file.configuration_option()
@click_config_file.configuration_option(implicit=True,provider=myprovider)
def cli():
    """ Generate a random password of length 12"""
    password = generate_password(length=12)
    print(f"Random generated password: {password}")

def generate_password(length=8, include_digits=True, include_uppercase=True, include_lowercase=True, include_punctuation=True):
    """
    Generate a random password based on the specified length and character categories.
    """
    characters = ""
    if include_digits:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_punctuation:
        characters += string.punctuation

    password = "".join(random.choice(characters) for i in range(length))

    return password

if __name__ == '__main__':
    cli() # pylint: disable=no-value-for-parameter # pragma: no cover

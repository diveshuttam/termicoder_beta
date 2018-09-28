import click
import os
import termicoder.data.config as config_data
import shutil
from ...utils.logging import logger


@click.command()
def main():
    """
    Initialize the config directory.
    """

    config_path = click.get_app_dir('termicoder')
    logger.info("Setting up configuration at '{config_dest}'".format(
        config_dest=config_path))

    if(os.path.exists(config_path)):
        click.confirm("Directory already exists. Overwrite?",
                      default=True, abort=True)
        shutil.rmtree(config_path)
    else:
        click.confirm("Continue", default=True, abort=True)

    # copy the config files into the path
    shutil.copytree(
        os.path.dirname(config_data.__file__), config_path,
        ignore=shutil.ignore_patterns('__init__.py', '__pycache__'))

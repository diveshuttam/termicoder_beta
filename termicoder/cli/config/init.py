import click
import os
import termicoder.data.config as config_data
import shutil


@click.command()
def main():
    """
    initialize the config directory for termicoder.
    """

    config_dest = click.get_app_dir('termicoder')
    click.echo("Setting up configuration at `{config_dest}`".format(
        config_dest=config_dest))

    if(os.path.exists(config_dest)):
        click.confirm("Directory already exists. Overwrite?",
                      default=True, abort=True)
        shutil.rmtree(config_dest)
    else:
        click.confirm("Continue", default=True, abort=True)

    # copy the config files into the path
    shutil.copytree(
        os.path.dirname(config_data.__file__), config_dest,
        ignore=shutil.ignore_patterns('__init__.py', '__pycache__'))

import click
import os


@click.command()
def main():
    """
    Edit the configuration.

    Launches the config folder for modifying settings.
    """

    config_path = click.get_app_dir('termicoder')
    if(os.path.exists(config_path)):
        click.launch(config_path)
    else:
        msg = "Could not find config folder: '{config_path}'\n".format(
            config_path=config_path) + "Run `termicoder config init` first!"
        raise click.UsageError(msg)

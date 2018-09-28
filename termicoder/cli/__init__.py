import click
import click_log
from .view import main as view
from . import code
from . import debug
from . import setup
from . import submit
from . import test
from . import repl
from . import config
from . import ls
from . import clip
from ..utils.logging import logger

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
@click_log.simple_verbosity_option(logger)
def main():
    '''
    \b
    __       __                      _                __
    \ \     / /____  _________ ___  (_)________  ____/ /__  _____
     \ \   / __/ _ \/ ___/ __ `__ \/ / ___/ __ \/ __  / _ \/ ___/
     / /  / /_/  __/ /  / / / / / / / /__/ /_/ / /_/ /  __/ /
    /_/   \__/\___/_/  /_/ /_/ /_/_/\___/\____/\__,_/\___/_/

    view, code & submit problems directly from terminal.
    '''


sub_commands = [
    {
        "cmd": code.main,
        "name": "code"
    },
    {
        "cmd": debug.main,
        "name": "debug"
    },
    {
        "cmd": setup.main,
        "name": "setup"
    },
    {
        "cmd": submit.main,
        "name": "submit"
    },
    {
        "cmd": test.main,
        "name": "test"
    },
    {
        "cmd": view,
        "name": "view"
    },
    {
        "cmd": repl.main,
        "name": "repl"
    },
    {
        "cmd": config.main,
        "name": "config"
    },
    {
        "cmd": ls.main,
        "name": "list"
    },
    {
        "cmd": clip.main,
        "name": "clip"
    }
]


for command in sub_commands:
    main.add_command(**command)


__all__ = ["main"]

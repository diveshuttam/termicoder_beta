import click

from .view import main as view
from . import code
from . import debug
from . import setup
from . import submit
from . import test
from . import repl
from . import config
from . import ls
from ..models.JudgeFactory import JudgeFactory

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug', is_flag=True, default=False,
              help='Turn on debug messages for Termicoder.', is_eager=True)
@click.version_option()
def main(debug):
    '''
    \b
    __       __                      _                __
    \ \     / /____  _________ ___  (_)________  ____/ /__  _____
     \ \   / __/ _ \/ ___/ __ `__ \/ / ___/ __ \/ __  / _ \/ ___/
     / /  / /_/  __/ /  / / / / / / / /__/ /_/ / /_/ /  __/ /
    /_/   \__/\___/_/  /_/ /_/ /_/_/\___/\____/\__,_/\___/_/

    view, code & submit problems directly from terminal.
    '''
    return None


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
    }
]


for command in sub_commands:
    main.add_command(**command)

JudgeFactory()

__all__ = ["main"]

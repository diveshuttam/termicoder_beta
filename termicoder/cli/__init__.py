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


# TODO print termicoder ascii art (termicoder.constants.ascii_art)
# by adding it correctly to click's help
@click.group()
def main():
    '''
    view, code & submit problems directly from terminal.
    '''
    pass


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

# TODO use sort __commands__ here so that no need to worry
# __commands__ is defined in __init__.py contains all commands bindings
# with their names
for command in sub_commands:
    main.add_command(**command)

__all__ = ["main"]

import click
from click_default_group import DefaultGroup

from . import contest
from . import problem
from . import this
from . import running
from ...utils.logging import logger
from ...utils.exceptions import handle_exceptions


# view command has various subcommands
# default is termicoder view this
# TODO change default_if_no_args to true
@click.group(cls=DefaultGroup, default='this', default_if_no_args=False)
@handle_exceptions(BaseException)
def main():
    '''
    View contests and problems.
    '''
    pass


sub_commands = [
    {
        "cmd": contest.main,
        "name": "contest"
    },
    {
        "cmd": problem.main,
        "name": "problem"
    },
    {
        "cmd": this.main,
        "name": "this"
    },
    {
        "cmd": running.main,
        "name": "running"
    }
]


for command in sub_commands:
    main.add_command(**command)

__all__ = ['main']

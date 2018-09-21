import click
from click_default_group import DefaultGroup

from . import contest
from . import problem
from . import this


# view command has various subcommands
# default is termicoder view this
# TODO change default_if_no_args to true
@click.group(cls=DefaultGroup, default='this', default_if_no_args=False)
def main():
    '''
    view contests, problems ad problem statement
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
    }
]


for command in sub_commands:
    main.add_command(**command)

__all__ = ['main']

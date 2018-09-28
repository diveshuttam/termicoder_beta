import click
from . import autocomplete
from . import init


@click.group()
def main():
    """
    Configure settings, autocomplete etc.
    """
#    raise NotImplementedError
#    eval(judge).setup(contest, problem, status)


sub_commands = [
    {
        "cmd": autocomplete.main,
        "name": "autocomplete"
    },
    {
        "cmd": init.main,
        "name": "init"
    }
]

for command in sub_commands:
    main.add_command(**command)

__all__ = ['main']

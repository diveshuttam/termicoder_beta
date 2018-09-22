import click
from . import autocomplete


OJs = []


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
    }
]

for command in sub_commands:
    main.add_command(**command)

__all__ = ['main']

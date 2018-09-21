import click
from . import __commands__ as commands


# view command has various subcommands
@click.group()
def main():
    '''
    view contests, problems and problem statement
    '''
    pass


for command_name in commands:
    main.add_command(**command_name)

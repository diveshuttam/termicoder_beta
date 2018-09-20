import click
from . import *

# view command has various subcommands
@click.group()
def main():
    '''
    view contests, problems and problem statement
    '''
    pass

for command_name in __commands__:
    main.add_command(command_name)
import click
from . import __commands__ as commands


# TODO print termicoder ascii art (termicoder.constants.ascii_art)
# by adding it correctly to click's help

@click.group()
def main():
    '''
    view, code & submit problems directly from terminal.
    '''


# __commands__ is defined in __init__.py contains all commands bindings
# with their names
for command in commands:
    main.add_command(**command)

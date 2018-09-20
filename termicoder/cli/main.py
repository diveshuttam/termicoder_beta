import click

# following line imports all commands in current folder
# refer __init__.py for more details
from termicoder.cli import *

# TODO print termicoder ascii art (termicoder.utils.constants.ascii_art)
# by adding it correctly to click's help
@click.group()
def main():
    '''

    view, code & submit problems directly from terminal.
    '''

# __commands__ is defined in __init__.py
for command_name in __commands__:
    main.add_command(**command_name)
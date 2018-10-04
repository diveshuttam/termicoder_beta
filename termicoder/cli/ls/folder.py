import click
from ...utils.logging import logger
from ...utils.exceptions import handle_exceptions
from ...utils.yaml import read
import subprocess


@click.command(short_help="View contents of folder.")
@click.argument("DIR", type=click.Path(
                    exists=True, file_okay=False, dir_okay=True), default='.')
@handle_exceptions(BaseException)
def main(dir):
    '''
    display the termicoder contents in current/passed folder

    \b
    if it is a contest folder it displays the list of problems.
    if its a problem folder, displays the problem in a browser.
    '''
    logger.warn('Dummy list in this version')
    subprocess.run(['ls', '-l', dir])

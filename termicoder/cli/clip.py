import click
import pyperclip
from ..utils.logging import logger
from ..utils.exceptions import handle_exceptions


@click.command(short_help='Copies code from file to clipboard.')
@click.argument('code_file',
                type=click.Path(writable=False, readable=True, dir_okay=False),
                required=False)
@handle_exceptions(BaseException)
def main(code_file):
    '''
    Copies code from CODE_FILE to the clipboard.

    If CODE_FILE is not passed, a default file is suggested based
    on current directory.

    The suggested file is the most recently edited code file
    recognized by termicoder.
    '''
    if(code_file is None):
        return
    pyperclip.copy(open(code_file, 'r').read())
    logger.info("copied %s to clipboard" % code_file)

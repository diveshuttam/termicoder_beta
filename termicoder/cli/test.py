import click
from ..utils.logging import logger
from ..utils.exceptions import handle_exceptions


@click.command()
@click.argument('code_file', type=click.File())
@click.option('-tl', '--timelimit', type=float,
              help="the max time per testcase")
@click.option('-l', '--live', is_flag=True, default=False,
              help="test the code live and don't use testcases")
def main(code_file, edit_scripts, timelimit, live):
    '''
    Test code against the sample testcases.

    \b
    this command (compiles and) runs passed code file.
    the code is run against all [.in] files in ./testcases folder.
    the output is produced in [.outx] files and checked against [.out] files

    it displays time for each testcase,status
    and diff of expected and produced outputs.
    '''
    raise NotImplementedError

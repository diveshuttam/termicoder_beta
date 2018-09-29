import click
from ..utils.logging import logger
from ..utils.exceptions import handle_exceptions

@click.command()
@click.option('-f', '--file', 'code_file', type=click.File(),
              help="the code file")
def main(code_file):
    '''
    Submit a solution.

    You should be in a problem directory to submit

    \b
    Script will prompt you to login into the judge(if not already).
    This submits the problem using data in [.problem] file in current directory
    '''
    raise NotImplementedError
    # judge = parse.get_judge()
    # if(not code_file):
    #     code_file = parse.get_code_file()
    # code_file = parse.get_file_name(code_file)
    # eval(judge).submit(code_file)

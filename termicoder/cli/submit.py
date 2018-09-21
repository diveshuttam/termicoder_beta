import click


@click.command()
@click.option('-f', '--file', 'code_file', type=click.File(),
              help="the code file")
def main(code_file):
    '''
    submit a solution.

    you should be in a problem directory to submit

    \b
    script will prompt you to login into the judge(if not already).
    this submits the problem using data in [.problem] file in current directory
    '''
    raise NotImplementedError
    # judge = parse.get_judge()
    # if(not code_file):
    #     code_file = parse.get_code_file()
    # code_file = parse.get_file_name(code_file)
    # eval(judge).submit(code_file)

import click


@click.command()
@click.option('-f', '--file', 'code_file', type=click.File(),
              help="the code file")
@click.option('-tl', '--timelimit', type=float,
              help="the max time per testcase")
@click.option('-l', '--live', is_flag=True, default=False,
              help="test the code live and don't use testcases")
@click.option('-es', "--edit_scripts", is_flag=True, default=False)
def main(code_file, edit_scripts, timelimit, live):
    '''
    test code against the sample testcases.

    \b
    this command (compiles and) runs passed code file.
    the code is run against all [.in] files in ./testcases folder.
    the output is produced in [.outx] files and checked against [.out] files

    it displays time for each testcase,status
    and diff of expected and produced outputs.
    '''
    raise NotImplementedError
    # if(edit_scripts):
    #     test_module.edit_scripts()

    # if(not code_file):
    #     code_file = parse.get_code_file()
    # code_file = parse.get_file_name(code_file)
    # test_module.test(code_file, timelimit, live)

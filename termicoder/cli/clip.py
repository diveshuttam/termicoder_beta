import click


@click.command()
@click.argument('FILE', 'code_file',
              type=click.Path(writable=False, readable=True, dir_okay=False),
              required=False)
def main(code_file, editor):
    '''
    Copies code from FILE to the clipboard.

    If FILE is not passed, a default file is suggested based
    on current directory.

    The suggested file is the most recently edited code file
    recognized by termicoder.
    '''
    raise NotImplementedError
    # if(edit_templates):
    #     code_module.edit_templates()

    # elif(edit_defaults):
    #     code_module.edit_defaults()

    # elif(code_file is None):
    #     code_file = code_module.get_file_name()

    # if(code_file is not None):
    #     code_module.code(code_file)

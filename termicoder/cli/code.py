import click
@click.command()
@click.option('-f', '--file', 'code_file',
              type=click.Path(writable=True, readable=False, dir_okay=False),
              help="the filename to code into with preloaded template")
@click.option('-et', "--edit_templates", is_flag=True, default=False,
              help="open templates folder")
@click.option('-ed', "--edit_defaults", is_flag=True, default=False,
              help="edit defaults for editors")
def main(code_file, edit_templates, edit_defaults):
    '''
    creates & open code file with template code.

    you can edit template code and default editors
    using flags -et and -ed respectively
    '''
    # if(edit_templates):
    #     code_module.edit_templates()

    # elif(edit_defaults):
    #     code_module.edit_defaults()

    # elif(code_file is None):
    #     code_file = code_module.get_file_name()

    # if(code_file is not None):
    #     code_module.code(code_file)


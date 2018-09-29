import click
from ..utils.exceptions import handle_exceptions

@click.command()
@click.argument('FILE', 'code_file',
              type=click.Path(writable=True, readable=False, dir_okay=False),
              required=False)
@click.option('--editor', type=click.STRING, help="Specify the editor to launch the file with.")
@handle_exceptions(BaseException)
def main(code_file, editor):
    '''
    Creates and opens FILE with template code.

    If FILE already exists, 'code' just opens it in the default
    default/supplied editor without any change.

    If FILE is not passed, a default name of file is suggested
    based on current directory, language preferences and existing
    files in directory.

    Default FILE is <PROBLEM_NAME>.<DEFAULT_EXTENSION> if user is
    in a problem folder and no other supported code file exists.
    If other code file(s) exist, it suggests to open the most
    recently edited one.

    Template for the code is loaded based upon extension.

    See 'termicoder config' for editing default templates,
    editor, and language preferences.
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

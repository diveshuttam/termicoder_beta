import click
from ..utils.exceptions import handle_exceptions
from ..utils import config
from ..utils import yaml
from ..utils.logging import logger
from ..utils.launch import launch
import os


@click.command(short_help='Creates and opens file with template code.')
@click.argument('code_file',
                type=click.Path(writable=True, readable=False, dir_okay=False),
                required=False)
@click.option('--editor',
              help="Specify the editor to launch the file with.",
              default=config.read('settings.yml', 'editor'))
@handle_exceptions(BaseException)
def main(code_file, editor):
    '''
    Creates and opens CODE_FILE with template code.

    If CODE_FILE already exists, 'code' just opens it in the default
    default/supplied editor without any change.

    If CODE_FILE is not passed, a default name of file is suggested
    based on current directory, language preferences and existing
    files in directory.

    Default CODE_FILE is <PROBLEM_NAME>.<DEFAULT_EXTENSION> if user is
    in a problem folder and no other supported code file exists.
    If other code file(s) exist, it suggests to open the most
    recently edited one.

    Template for the code is loaded based upon extension.

    See 'termicoder config' for editing default templates,
    editor, and language preferences.
    '''
    if code_file is None:
        default_name = config.read('settings.yml', 'default_code_file')
        if ".problem.yml" in os.listdir():
            problem = yaml.read('.problem.yml')
            default_name = problem.code + "." + config.read(
                'settings.yml', 'default_extension')

        code_file = click.prompt(
            "Please enter a file name", default=default_name)

    extension = code_file.split('.')[-1]
    template = config.read('code/templates/%s/template.yml' % extension)

    if(template is not None):
        try:
            code_to_write = template['code']
            # allow jinja style template substitution in command
            # example {{row_no}} and {{col_no}}
            if(isinstance(editor, list)):
                for key in template:
                    value = template[key]
                    editor = [
                        args.replace("{{%s}}" % key, str(value)) for
                        args in editor
                    ]
                    logger.debug(editor)
            logger.debug(code_to_write)
        except (AttributeError, KeyError):
            raise
    else:
        logger.warn("You don't have templates setup for extension %s "
                    "Launching empty file " % extension)
    if(not os.path.exists(code_file)):
        code = click.open_file(code_file, 'w')
        code.write(code_to_write)
    launch(editor, code_file)

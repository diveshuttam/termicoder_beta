import click


@click.command(short_help="View contents of current folder")
@click.argument("DIR", type=click.Path(
                               exists=True, file_okay=False, dir_okay=True),
                default='.')
@click.option("-ed", "--edit_defaults", is_flag=True, default=False,
              help="edit default web browser")
def main(dir, edit_defaults):
    '''
    display the termicoder contents in current/passed folder

    \b
    if it is a contest folder it displays the list of problems.
    if its a problem folder, displays the problem in a browser.
    '''
    raise NotImplementedError
    # viewthis_module.view(folder, edit_defaults)

import click
@click.command(short_help="view contents of current folder")
@click.option("-f", "--folder", type=click.Path())
@click.option("-ed", "--edit_defaults", is_flag=True, default=False,
              help="edit default web browser")
def main(folder, edit_defaults):
    '''
    display the termicoder contents in current/passed folder

    \b
    if it is a contest folder it displays the list of problems.
    if its a problem folder, displays the problem in a browser.
    '''
    viewthis_module.view(folder, edit_defaults)

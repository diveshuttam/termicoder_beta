import click

OJs=[]
@click.command(short_help="display contest list of a judge")
@click.option('-j', '--judge', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")")
def main(judge):
    '''
    lists current and upcoming contests on a judge.

    depending on judge it may give a list of categories also
    such as PRACTICE etc.
    '''
    # eval(judge).view_contests()
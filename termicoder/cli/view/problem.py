import click
OJs = []


@click.command(short_help="list problems of a contest/category")
@click.option('-j', '--judge', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")")
@click.option('-c', '--contest', type=click.STRING, help="contest code")
def main(judge, contest):
    '''
    lists problems of a contest/category on the judge
    '''
    raise NotImplementedError
    # eval(judge).view_problems(contest)

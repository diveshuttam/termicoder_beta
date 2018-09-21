import click

OJs = []


@click.group()
@click.option('-j', '--judge', type=click.Choice(OJs))
#              prompt="Please provide a judge("+'|'.join(OJs)+")")
@click.option('-c', '--contest', type=click.STRING, help="contest code")
@click.option('-p', '--problem', type=click.STRING, help="problem code")
@click.option('--login', 'status', flag_value='login')
@click.option('--logout', 'status', flag_value='logout')
def main(judge, contest, problem, status):
    """
    sets up problem, contests and login.

    1. if you pass judge and --login/--logout,
    it logs you in and out of the judge

    2. if you pass judge and contest/category
    it downloads all the problems of that contest.

    3. if you pass a particular problem, with judge and contest/category,
    it sets up that problem.

    all this happens in the current folder.
    option of contest/category may vary amongst various online judges
    """
    raise NotImplementedError
    # eval(judge).setup(contest, problem, status)


__all__ = ['main']

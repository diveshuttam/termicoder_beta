import click
from ...models import JudgeFactory
from ...utils.setup import output_problem, output_contest
from ...utils.constants import default_judge

judge_factory = JudgeFactory()
OJs = judge_factory.available_judges


@click.command()
@click.option('-j', '--judge', 'judge_name', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")",
              default=default_judge)
@click.option('-c', '--contest', type=click.STRING, help="contest code")
@click.option('-p', '--problem', type=click.STRING, help="problem code")
@click.option('--login', 'status', flag_value='login')
@click.option('--logout', 'status', flag_value='logout')
def main(judge_name, contest, problem, status):
    """
    Sets up problem, contests and login.

    1. If you pass judge and --login/--logout,
    it logs you in and out of the judge

    2. If you pass judge and contest/category
    it downloads all the problems of that contest.

    3. if you pass a particular problem, with judge and contest/category,
    it sets up that problem.

    all this happens in the current folder.
    option of contest/category may vary amongst various online judges
    """

    # TODO judge.check_login and print current status
    judge = judge_factory.get_judge(judge_name)

    if(status == 'login'):
        judge.login()
    elif(status == 'logout'):
        judge.logout()
        return

    if(problem):
        problem = judge.get_problem(contest_name=contest, problem_name=problem)
        problem_directory = "."
        output_problem(problem, problem_directory)
    elif(contest and not problem):
        contest = judge.get_contest(contest_name=contest)
        contest_directory = "."
        output_contest(contest, contest_directory)


__all__ = ['main']

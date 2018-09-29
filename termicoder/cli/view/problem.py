import click
from ...models import JudgeFactory
from ...utils.constants import default_judge

judge_factory = JudgeFactory()
OJs = judge_factory.available_judges

@click.command(short_help="View a particular problem")
@click.option('-j', '--judge', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")",
              default=default_judge)
@click.option('-c', '--contest', type=click.STRING, help="contest code")
def main(judge, contest):
    '''
    View a particular problem from the judge.
    '''
    raise NotImplementedError
    # eval(judge).view_problems(contest)

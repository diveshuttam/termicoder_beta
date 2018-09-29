import click
from ...models import JudgeFactory
from ...utils.constants import default_judge

judge_factory = JudgeFactory()
OJs = judge_factory.available_judges


@click.command(short_help="Display a particular contest")
@click.option('-j', '--judge', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")",
              default=default_judge)
def main(judge):
    '''
    View a particular contest.

    depending on judge it may give a list of categories also
    such as PRACTICE etc.
    '''
    raise NotImplementedError

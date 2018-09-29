import click
from ...models import JudgeFactory
from ...utils.constants import default_judge
from ...utils.logging import logger
from ...utils.exceptions import handle_exceptions

judge_factory = JudgeFactory()
OJs = judge_factory.available_judges


@click.command(short_help="Display a particular contest")
@click.option('-j', '--judge', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")",
              default=default_judge)
@handle_exceptions(BaseException)
def main(judge):
    '''
    View a particular contest.

    depending on judge it may give a list of categories also
    such as PRACTICE etc.
    '''
    raise NotImplementedError

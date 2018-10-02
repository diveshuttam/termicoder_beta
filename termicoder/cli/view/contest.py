import click
from ...models import JudgeFactory
from ...utils.constants import default_judge
from ...utils.logging import logger
from ...utils.exceptions import handle_exceptions
from ...utils import config
from ...utils.launch import launch

judge_factory = JudgeFactory()
OJs = judge_factory.available_judges


@click.command(short_help="Display a particular contest")
@click.option('-j', '--judge', 'judge_name', type=click.Choice(OJs),
              prompt="Please provide a judge("+'|'.join(OJs)+")",
              default=default_judge)
@click.option("--browser", help='Browser to launch', type=click.STRING,
              default=config.read('settings.yml', 'browser'))
@click.argument('contest')
@handle_exceptions(BaseException)
def main(judge_name, contest, browser):
    '''
    View a particular problem from the judge.
    '''
    judge = judge_factory.get_judge(judge_name)
    contest_url = judge.get_contest_url(contest_code=contest)
    logger.debug('launching %s' % contest_url)
    launch(browser, contest_url)

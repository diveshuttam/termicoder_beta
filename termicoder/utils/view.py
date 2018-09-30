from .logging import logger
import click


def folder(dir, browser):
    # if .problem in current folder
    #     problem = yaml.load()
    #     launch problem html in default browser
    # else if .contest in current folder
    #     contest = yaml.load()
    #     launch a server in current directory
    # TODO later migrate to flask based server
    url = None
    if browser is None:
        logger.warn('preferred browser not set, launching in default browser')
        click.launch(url)
    else:
        logger.info('Launching problem with %s' % browser)



def problem_folder():
    raise NotImplementedError


def contest_folder():
    raise NotImplementedError

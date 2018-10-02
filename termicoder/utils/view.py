from .logging import logger
import click
import os
from . import yaml
import subprocess


def folder(directory, browser):
    # TODO later migrate to flask based server
    logger.debug(os.listdir(directory))
    url = None
    if '.problem.yml' in os.listdir(directory):
        problem = yaml.read(os.path.join(directory, '.problem.yml'))
        url = os.path.join(directory, "%s.html" % problem.code)

    elif '.contest.yml' in os.listdir(directory):
        contest = yaml.read(os.path.join(directory, '.contest.yml'))
        logger.debug('launching contest %s' % contest.name)
        url = directory

    else:
        logger.error(".problem.yml and .contest.yml not found in folder")
        logger.error("Please make sure you are in correct directory")
        return

    if browser is None:
        logger.warn('preferred browser not set, launching in default browser')
        click.launch(url)
    else:
        logger.info('Launching problem with %s' % browser)
        subprocess.call([browser, url])

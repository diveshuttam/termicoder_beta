import click
import subprocess
from .logging import logger


def launch(app_args, url):
    if(app_args is None):
        logger.warn('Preferred application is not set,'
                    'launching %s in default application' % url)
        click.launch(url)
    else:
        args = app_args
        if(not isinstance(app_args, list)):
            args = [app_args]
        logger.info('Launching %s with %s' % (url, ' '.join(args)))
        if url not in [None, '']:
            args.append(url)
        logger.debug(args)
        subprocess.run(args)

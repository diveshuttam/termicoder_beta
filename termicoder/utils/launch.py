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
        subprocess.run(args, shell=True)


def substitute(args, keymap):
    logger.debug('in substitute args')
    if args is not None:
        if(not (isinstance(args, list))):
            orig_args = args[:]
            for key in keymap:
                value = keymap[key]
                args = args.replace("{{%s}}" % key, str(value))
        else:
            orig_args = args[:]
            for key in keymap:
                value = keymap[key]
                args = [
                    arg.replace("{{%s}}" % key, str(value)) for
                    arg in args
                ]
    logger.warn(keymap)
    logger.debug("args")
    logger.debug(args)
    return (orig_args != args, args)

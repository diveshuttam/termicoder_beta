import click
from . import autocomplete


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
    configure termicoder settings, autocomplete etc.
    """
#    raise NotImplementedError
    # eval(judge).setup(contest, problem, status)


sub_commands = [
    {
        "cmd": autocomplete.main,
        "name": "autocomplete"
    }
]

for command in sub_commands:
    main.add_command(**command)

__all__ = ['main']

import click
from ..utils.logging import logger
from ..utils.exceptions import handle_exceptions
from ..utils.load import get_default_code_name
from ..models import JudgeFactory
from ..utils import config
from ..utils import yaml
import subprocess
import os
judge_factory = JudgeFactory()


@click.command()
@click.argument('code_file', type=click.Path(exists=True, dir_okay=False))
@click.option('-tl', '--timelimit', type=float,
              help="the max time per testcase")
@click.option('-l', '--live', is_flag=True, default=False,
              help="test the code live and don't use testcases")
@handle_exceptions(BaseException)
def main(code_file, edit_scripts, timelimit, live):
    '''
    Test code against the sample testcases.

    \b
    this command (compiles and) runs passed code file.
    the code is run against all [.in] files in ./testcases folder.
    the output is produced in [.outx] files and checked against [.out] files

    it displays time for each testcase,status
    and diff of expected and produced outputs.
    '''
    if '.problem.yml' not in os.listdir():
        logger.error("You should be in a problem directory to test")
        return
    else:
        problem = yaml.read('.problem.yml')
        judge = judge_factory.get_judge(problem.judge_name)

    if not ('testcases' in os.listdir() and os.path.isdir('testcases')):
        logger.error("No testcases directory in the folder")
        # run with option --live
        return

    if(code_file is None):
        default_file = get_default_code_name()
        if (not os.path.exists(default_file)):
            default_file = None
        code_file = click.prompt(
            "Please a code file to test",
            default=default_file,
            type=click.Path(readable=True, exists=True, dir_okay=False)
        )

    build_name, extension = code_file.split(".")[-1]

    # this envs may be used in build scripts
    os.environ['TERMICODER_EXTENSION'] = extension
    os.environ['TERMICODER_FILE_NAME'] = code_file
    os.environ['TERMICODER_BUILD_NAME'] = build_name

    test_config = config.read('lang/%s/test.yml')
    if(test_config is None):
        logger.error(
            "No build configurations found for .%s files" % extension
        )
        raise click.Abort

    try:
        build_command = test_config['build']
        run_command = test_config['run']
    except KeyError:
        logger.error("Invalid test.yml")
        raise click.Abort

    # build the file
    # build_commands may be None for interpreted languages
    if build_command is not None:
        if(not isinstance(build_command, list)):
            build_command = [build_command]
        try:
            p = subprocess.run(build_command, check=True)
        except subprocess.CalledProcessError:
            logger.error('Compile Time Error!')
            return


    # for testing output with input
    # TODO if no .in files, then run --live
    # maybe  move the checking functionality to problem class
    # helpful for interactive problems
    for testcase_file in os.listdir('testcases'):
        if(testcase_file.endswith('.in')):
            name = testcase_file.split('.')[0]
            inp_file = click.open_file("%s.in" % name)
            inp = inp_file.read()
            ans_file = click.open_file("%s.ans" % name)
            ans = ans_file.read()
            out_file = click.open_file("%s.out" % name)
            testcase = judge.get_testcase(inp=inp, ans=ans)
            if(not isinstance(run_command, list)):
                args = [run_command]
            try:
                p = subprocess.run(args, capture_output=True,
                                   timeout=problem.timeout, output=out_file)
                out = p.output
            except subprocess.TimeoutExpired:
                logger.error('TimeLimitExceeded!')
                return
            except subprocess.CalledProcessError:
                logger.error('RunTimeError!')
                return
            else:
                testcase.diff(out)

    raise NotImplementedError

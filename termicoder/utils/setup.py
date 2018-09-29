from ..models import Problem
from ..models import Contest
from ..models import Testcase
from .logging import logger
from ..utils.config import write


def output_testcases(testcase, testcase_dir):
    # TODO output testcases
    assert isinstance(testcase, Testcase)
    raise NotImplementedError


def output_problem(problem, problem_dir):
    # TODO output
    # .problem(problem_data, problem_name, contest_name, judge_name)
    # output testcases
    assert isinstance(problem, Problem)
    Problem.problem_code



def output_contest(contest, contest_dir):
    # TODO output .contest(contest_data, contest_name, judge_name)
        # for each problem:
        #   output problem_data
        #   output testcases
    assert isinstance(contest, Contest)
    raise NotImplementedError

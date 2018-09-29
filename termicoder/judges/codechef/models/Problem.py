#!/usr/bin/python
# -*- coding: utf-8 -*-

from termicoder.models import Problem


class CodechefProblem(Problem):
    def __init__(self, problem_data=None):
        self.problem_data = problem_data
        self.isSolved = None
        self.isAttempted = None
        self.tags = None
        self.author = None
        self.date_added = None

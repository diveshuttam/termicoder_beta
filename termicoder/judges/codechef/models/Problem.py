#!/usr/bin/python
# -*- coding: utf-8 -*-

from termicoder.models import Problem
from collections import namedtuple


class CodechefProblem(Problem):
    def __init__(self, data=None):
        self.isSolved = None
        self.isAttempted = None
        self.tags = None
        self.author = None
        self.date_added = None
        self.code = None
        self.data = data
        self.html = None
        if(data is not None):
            self._initialize()

    def _initialize(self):
        concerned_data = self.data['result']['data']['content']
        problem_content = namedtuple(
            "problem", concerned_data.keys())(*concerned_data.values())
        self.code = problem_content.problemCode
        self.html = problem_content.body

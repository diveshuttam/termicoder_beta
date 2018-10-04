#!/usr/bin/python
# -*- coding: utf-8 -*-
from termicoder.models import Contest
from collections import namedtuple


class CodechefContest(Contest):
    def __init__(self, data):
        self.code = None
        self.problems = []
        self.data = data
        self.judge_name = "codechef"
        self.problem_codes = []
        if(data is not None):
            self._initialize()

    def _initialize(self):
        concerned_data = self.data['result']['data']['content']
        content = namedtuple(
            "problem", concerned_data.keys())(*concerned_data.values())
        self.code = content.code
        self.problem_codes = [x['problemCode'] for x in content.problemsList]

    def __str__(self):
        pass

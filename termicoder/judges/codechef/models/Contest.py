#!/usr/bin/python
# -*- coding: utf-8 -*-
from termicoder.models import Contest
from collections import namedtuple


class CodechefContest(Contest):
    def __init__(self, data):
        self.name = None
        self.url = None
        self.start_time = None
        self.end_time = None
        self.problems = []
        self.data = data
        self.problem_codes = []
        self.contests_url = 'https://www.codechef.com/contests/'
        if(data is not None):
            self._initialize()

    def _initialize(self):
        concerned_data = self.data['result']['data']['content']
        content = namedtuple(
            "problem", concerned_data.keys())(*concerned_data.values())
        self.code = content.code
        self.problem_codes = [x['problemCode'] for x in content.problemsList]

    def getProblems(self):
        pass

    def refresh(self):
        pass

    def ls(self):
        pass

    def view(self):
        pass

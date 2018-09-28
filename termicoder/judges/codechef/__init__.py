#!/usr/bin/python
# -*- coding: utf-8 -*-
from ...models import Judge
from . import utils


class Codechef(Judge):
    def __init__(self, session_data=None):
        # Init should not have any network requests
        # do them in login, logout, check_running_contest
        self.name = None
        self.url = None
        self.user = None
        self.session_data = session_data

    def check_login(self):
        raise NotImplementedError

    def login(self):
        token = utils.login_client()
        self.session_data = token

    def logout(self):
        raise NotImplementedError

    def get_running_contests(self):
        raise NotImplementedError

    # This method serves both as a problem getter as well as kind of factory
    # for problem
    def get_problem(self, problem_name, contest_name, problem_data=None):
        # If problem data is passed, it should take precedence
        # Method should call the respective Problem.__init__ method to create a
        # problem instance and return it
        raise NotImplementedError

    def get_contest(self, contest_name, contest_data=None):
        # If contest data is passed, it should take precedence
        # Method should call the respective Problem.__init__ method to create a
        # problem instance and return it
        pass

#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod

# Judge is an abstract class implemented by Judge developers
# Judge kind of doubles up for login logout as well as a Factory
# For the contest and problem classes for the particular judge
class Judge(ABC):
    @abstractmethod
    def __init__(self, session_data=None):
        self.name = None
        self.url = None
        self.user = None
        self.session_data = session_data

    @abstractmethod
    def check_login(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def get_running_contests(self):
        pass

    @abstractmethod
    def get_problem(self, problem_name, contest_name, problem_data=None):
        pass

    @abstractmethod
    def get_contest(self, contest_name, contest_data=None):
        pass

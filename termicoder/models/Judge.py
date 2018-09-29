#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod


# Judge is an abstract class to be subclassed and implemented
# by Judge developers.

# Judge class kind of doubles up for login-logout as well as a Factory
# for the contest and problem classes for the particular judge
class Judge(ABC):
    @abstractmethod
    def __init__(self, session_data=None):
        # Init should not have any network requests
        # do them in login, logout, check_running_contest
        self.session_data = session_data

    @abstractmethod
    def check_login(self):
        pass

    @abstractmethod
    def login(self):
        # login also controls all the messages being displayed to the user
        pass

    @abstractmethod
    def logout(self):
        # logout also controls all the messages displayed to the user
        pass

    @abstractmethod
    def get_running_contests(self):
        pass

    # This method serves both as a problem getter as well as kind of factory
    # for problem
    @abstractmethod
    def get_problem(self, problem_name, contest_name, problem_data=None):
        # If problem data is passed, it should take precedence
        # Method should call the respective Problem.__init__ method to create a
        # problem instance and return it
        pass

    @abstractmethod
    def get_contest(self, contest_name, contest_data=None):
        # If contest data is passed, it should take precedence
        # Method should call the respective Problem.__init__ method to create a
        # problem instance and return it
        pass

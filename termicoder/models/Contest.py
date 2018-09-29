#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod


class Contest(ABC):
    @abstractmethod
    def __init__(self, contest_code, problems=None, data=None):
        # If contest_data, problems is passed, it should take priority
        self.code = contest_code
        self.problems = problems
        self.data = data
        if(data is None):
            self.refresh()

    @abstractmethod
    def refresh(self, ):
        # get problems etc.
        pass

    @abstractmethod
    def ls(self):
        # return strings which would be printed to terminal
        pass

    @abstractmethod
    def view(self):
        # return html which would be displayed in the browser
        pass

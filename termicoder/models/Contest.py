#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod

class Contest(ABC):
    @abstractmethod
    def __init__(self):
        self.name = None
        self.url = None
        self.start_time = None
        self.end_time = None
        self.problems = None

    def getProblems(self, ):
        pass

    def refreshContest(self, ):
        pass

    def view_local(self, ):
        pass

    def view_online():
        pass

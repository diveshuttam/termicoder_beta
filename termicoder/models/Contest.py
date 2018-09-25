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


    @abstractmethod
    def get_problems(self, ):
        pass

    @abstractmethod
    def refresh_contest(self, ):
        pass

    @abstractmethod
    def view_local(self):
        pass

    @abstractmethod
    def view_online(self):
        pass

    @abstractmethod
    def save_local(self):
        pass

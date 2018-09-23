#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod

# Judge is an abstract class implemented by Judge developers
class Judge(ABC):
    @abstractmethod
    def __init__(self):
        self.name = None
        self.url = None
        self.user = None

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def getRunningContests(self, ):
        pass

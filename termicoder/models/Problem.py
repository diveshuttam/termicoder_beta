#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def __init__(self, data):
        self.isSolved = None
        self.isAttempted = None
        self.tags = None
        self.author = None
        self.date_added = None
        self.data = data
        self.code = None

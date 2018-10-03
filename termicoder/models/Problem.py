#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def __init__(self, data):
        self.data = data
        self.code = None
        self.timelimit = 3.0  # in seconds

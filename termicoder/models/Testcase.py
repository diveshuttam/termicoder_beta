#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod
import difflib


class Testcase(ABC):
    @abstractmethod
    def __init__(self, ans, inp, code):
        self.ans = ans
        self.inp = inp
        self.code = code

    # judges can override this if they want
    # this is used to produce diff on termicoder test
    def diff(self, out):
        return difflib.diff(self.ans, self.out)

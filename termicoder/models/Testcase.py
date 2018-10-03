#!/usr/bin/python
# -*- coding: utf-8 -*-

# ABC is the AbstractBaseClass in python
from abc import ABC, abstractmethod


class Testcase(ABC):
    @abstractmethod
    def __init__(self, ans, inp, code):
        self.ans = ans
        self.inp = inp
        self.code = code

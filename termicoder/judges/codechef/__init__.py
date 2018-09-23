from ...models import Judge
#!/usr/bin/python
# -*- coding: utf-8 -*-


class Codechef(Judge):
    def __init__(self):
        self.name = None
        self.url = None
        self.user = None

    def login(self, ):
        pass

    def logout(self,):
        pass

    def getRunningContests(self, ):
        pass

    def setupContest(self, contest_code):
        pass

    def setupProblem(self, problem_code):
        pass

    def submit(self, ):
        pass

__all__ = ['Codechef']

from ...models import Judge
#!/usr/bin/python
# -*- coding: utf-8 -*-


class Codechef(Judge):
    def __init__(self):
        self.name = None
        self.url = None
        self.user = None

    def login(self, ):
        raise NotImplementedError

    def logout(self,):
        raise NotImplementedError

    def get_running_contests(self, ):
        raise NotImplementedError

    def get_contest(self, contest_code):
        raise NotImplementedError

    def get_problem(self, contest_code, problem_code):
        raise NotImplementedError

    def submit(self, ):
        pass

__all__ = ['Codechef']

from ...models import Judge
#!/usr/bin/python
# -*- coding: utf-8 -*-


class Iarcs(Judge):
    def __init__(self):
        self.name = None
        self.url = None
        self.user = None

    def check_login(self):
        pass

    def login(self, ):
        pass

    def logout(self,):
        pass

    def get_running_contests(self, ):
        pass

    def get_contest(self, contest_code):
        pass

    def get_problem(self, problem_code):
        pass

    def submit(self, problems):
        pass

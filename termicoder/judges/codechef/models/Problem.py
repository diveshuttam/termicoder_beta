from termicoder.models import Problem
from termicoder.utils.logging import logger
from collections import namedtuple
import markdown
import os
from ..utils.testcases import extract


class CodechefProblem(Problem):
    def __init__(self, data=None):
        self.isSolved = None
        self.isAttempted = None
        self.tags = None
        self.author = None
        self.date_added = None
        self.code = None
        self.data = data
        self.html = None
        self.testcases = None
        self.judge_name = "codechef"
        self.timelimit = 3.0
        if(data is not None):
            self._initialize()

    def _initialize(self):
        concerned_data = self.data['result']['data']['content']
        problem_content = namedtuple(
            "problem", concerned_data.keys())(*concerned_data.values())
        self.code = problem_content.problemCode
        self.html = self._get_html(problem_content.body)
        self.testcases = self._extract_testcases(self.html)
        self.timelimit = problem_content.maxTimeLimit

    def _get_html(self, body):
        newbody = body.replace('<br>', '\n')
        newbody = newbody.replace('<br />', '\n')
        mdProcessor = markdown.Markdown()
        myHtmlFragment = str(mdProcessor.convert(newbody))
        myHtmlFragment = myHtmlFragment.replace('<code>', '<pre>')
        myHtmlFragment = myHtmlFragment.replace('</code>', '</pre>')
        logger.debug(myHtmlFragment)
        javascript = open(
            os.path.join((os.path.dirname(__file__)), "script.js")).read()
        return ("<script>%s</script>" % javascript) + myHtmlFragment

    def _extract_testcases(self, html):
        testcases = extract(html)
        return testcases

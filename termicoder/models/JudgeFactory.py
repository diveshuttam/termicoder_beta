# for loading judge plugins
from pkg_resources import iter_entry_points
from . import Judge
from ..utils.Errors import JudgeNotFoundError


class JudgeFactory:
    def __init__(self):
        self.available_judges = []
        self._judge_classes = []
        self._load_judges()

    def _load_judges(self):
        judges = iter_entry_points('termicoder.judge_plugins')
        for judge in judges:
            try:
                judge_class = judge.load()
                assert(issubclass(judge_class, Judge))
                # Try instantiating judge to check if abstract methods are implemented
                judge_class()
                self.available_judges.append(judge.name)
            # TODO log about 'why could not load judge'
            except AssertionError as e:
                # Not a subclass
                pass
            except TypeError as e:
                # Abstract methods are not implemented
                pass
            except:
                raise

        # sorting judges for statefulness
        self.available_judges.sort()

    def get_judge(self, judge_name):
        if(judge_name not in available_judges):
            raise JudgeNotFoundError
        else:
            # Return an instance of the judge
            return self._judge_classes[judge_name]()

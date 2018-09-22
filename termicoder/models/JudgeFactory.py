# for loading judge plugins
from pkg_resources import iter_entry_points
from .Judge import Judge


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
                self.available_judges.append(judge.name)
            except BaseException as e:
                raise
                print(e)
                # TODO log about 'why could not load judge'
                pass
        # sorting judges for statefulness
        self.available_judges.sort()

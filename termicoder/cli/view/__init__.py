from . import contest
from . import problem
from . import this

__commands__ = [
    {
        "cmd": contest.main,
        "name": "contest"
    },
    {
        "cmd": problem.main,
        "name": "problem"
    },
    {
        "cmd": this.main,
        "name": "this"
    }
]
# TODO sort __commands__ here by command name
__all__ = ["__commands__"]

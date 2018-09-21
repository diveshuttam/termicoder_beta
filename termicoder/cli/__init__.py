from .view import main as view
from . import code
from . import debug
from . import setup
from . import submit
from . import test

__commands__ = [
    {
        "cmd": code.main,
        "name": "code"
    },
    {
        "cmd": debug.main,
        "name": "debug"
    },
    {
        "cmd": setup.main,
        "name": "setup"
    },
    {
        "cmd": submit.main,
        "name": "submit"
    },
    {
        "cmd": test.main,
        "name": "test"
    },
    {
        "cmd": view.main,
        "name": "view"
    }
]

# TODO use sort __commands__ here so that no need to worry
__all__ = ["__commands__"]

from .view.main import main as view
from .code import main as code
from .debug import main as debug
from .setup import main as setup
from .submit import main as submit
from .test import main as test

__commands__ = [
    {
        "cmd": code,
        "name": "code"
    },
    {
        "cmd": debug,
        "name": "debug"
    },
    {
        "cmd": setup,
        "name": "setup"
    },
    {
        "cmd": submit,
        "name": "submit"
    },
    {
        "cmd": test,
        "name": "test"
    }
]
# TODO use sort __commands__ here so that no need to worry
__all__ = ["code", "debug", "setup", "submit", "view", "__commands__"]
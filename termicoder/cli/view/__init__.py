from .contest import main as contest
from .problem import main as problem
from .this import main as this

__commands__ = [contest, problem, this]
__all__ = ["contest", "problem", "this", "__commands__"]

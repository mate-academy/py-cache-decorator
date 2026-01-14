from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    """
    Caches function results based on arguments to avoid recomputation.
    Works with hashable positional and keyword arguments.
    """
    cached = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> object:
        key = (args, frozenset(kwargs.items()))
        if key in cached:
            print("Getting from cache")
            return cached[key]

        print("Calculating new result")
        res = func(*args, **kwargs)
        cached[key] = res
        return res

    return wrapper

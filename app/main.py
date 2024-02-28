from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = {}

    @wraps(func)
    def inner(*args: tuple) -> Callable:
        name = (func.__name__, args)
        if name in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[name] = func(*args)
        return cached[name]
    return inner

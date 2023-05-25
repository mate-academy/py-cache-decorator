from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = {}

    @wraps(func)
    def inner(*args) -> Callable:
        if args in cached:
            print("Getting from cache")
            return cached[args]
        else:
            result = func(*args)
            cached[args] = result
            print("Calculating new result")
            return result
    return inner

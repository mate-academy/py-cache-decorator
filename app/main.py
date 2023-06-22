import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        return results[key]

    return inner

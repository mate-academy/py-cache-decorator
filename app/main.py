import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return inner

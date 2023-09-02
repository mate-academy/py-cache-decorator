import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))

        if key in cache_result:
            print("Getting from cache")
            return cache_result[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_result[key] = result
            return result

    return wrapper

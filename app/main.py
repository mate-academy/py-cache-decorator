import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in cache:
            print("Getting from cache")
            return cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
    return wrapper

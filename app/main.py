from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_d = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_d:
            print("Getting from cache")
            return cache_d[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_d[key] = result
            return result

    return wrapper

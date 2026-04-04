from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_history = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_history:
            print("Getting from cache")
            return cache_history[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_history[key] = result
            return result
    return inner

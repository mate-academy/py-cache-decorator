import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))
        if func.__name__ not in cache_list:
            cache_list[func.__name__] = {}

        if key in cache_list[func.__name__]:
            print("Getting from cache")
            return cache_list[func.__name__][key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_list[func.__name__][key] = result
            return result
    return inner

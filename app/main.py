import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in dict_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_cache[args] = func(*args)
        return dict_cache[args]
    return wrapper

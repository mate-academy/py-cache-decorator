from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args) -> dict:
        if args not in cache_dict:
            cache_dict[args] = func(args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]
    return inner

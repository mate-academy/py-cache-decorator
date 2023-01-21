from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: tuple) -> Callable:
        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper

from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (func, args, tuple(kwargs.items()))

        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[key]

    return wrapper

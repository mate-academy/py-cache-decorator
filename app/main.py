from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def cache_wrapper(*args, **kwargs) -> dict:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_dict[key]
        print("Getting from cache")
        return cache_dict[key]
    return cache_wrapper

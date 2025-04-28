from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        keys = (args, tuple(sorted(kwargs.items())))
        if keys in cache_dict:
            print("Getting from cache")
            return cache_dict[keys]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache_dict[keys] = res
            return res
    return wrapper

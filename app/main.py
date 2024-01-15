from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        args_tuple = args + tuple(sorted(kwargs.items()))
        if args_tuple in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args_tuple] = func(*args, **kwargs)
        return cache_dict[args_tuple]

    return wrapper

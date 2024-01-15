from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        args_tuple = args + tuple(sorted(kwargs.items()))
        if args_tuple in cache_dict:
            print("Getting from cache")
            return cache_dict[args_tuple]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            cache_dict[args_tuple] = result
            return result

    return wrapper

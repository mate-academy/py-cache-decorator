from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> dict:
        key = (args, tuple(kwargs.items()))
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            cache_func = func(*args, **kwargs)
            result[key] = cache_func
            print("Calculating new result")
            return cache_func

    return wrapper
    pass

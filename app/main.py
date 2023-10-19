from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (func, args, tuple(kwargs.items()))

        if key not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
            result = cache_dict[key]

        return result

    return wrapper

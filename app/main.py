from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> None:
        key = (args, tuple(kwargs.items()))
        if key not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
        print("Getting from cache")
        return cache_dict[key]
    return inner

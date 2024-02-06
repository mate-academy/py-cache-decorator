from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_info = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_info:
            print("Getting from cache")
            return cache_info[key]
        else:
            result = func(*args, **kwargs)
            cache_info[key] = result
            print("Calculating new result")
            return result
    return inner

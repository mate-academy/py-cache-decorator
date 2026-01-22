from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_immutable_values = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        cache_key = (func, args, tuple(kwargs.items()))

        if cache_key in cache_immutable_values:
            print("Getting from cache")
            return cache_immutable_values[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_immutable_values[cache_key] = result
            return result
    return inner

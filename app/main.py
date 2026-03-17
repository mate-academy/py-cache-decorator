from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_data = {}

    if func.__name__ not in cache_data:
        cache_data[func.__name__] = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        if (*args, frozenset(kwargs)) in cache_data[func.__name__]:
            print("Getting from cache")
            return cache_data[func.__name__][*args, frozenset(kwargs)]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[func.__name__][*args, frozenset(kwargs)] = result

        return result

    return inner

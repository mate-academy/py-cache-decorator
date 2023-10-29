from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]

        result = func(*args, **kwargs)
        cache_store[key] = result
        print("Calculating new result")
        return result

    return wrapper

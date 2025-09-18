from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> object:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[key] = result
        return result

    return wrapper

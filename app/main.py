from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    storage_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key not in storage_cache:
            result = func(*args, **kwargs)
            storage_cache[key] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return storage_cache[key]
    return wrapper

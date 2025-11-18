from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    new_cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in new_cache:
            print("Getting from cache")
            return new_cache[cache_key]
        else:
            print("Calculating new result")
        result = func(*args, **kwargs)
        new_cache[cache_key] = result
        return result
    return wrapper

from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        cache_key = (func.__name__, args, frozenset(kwargs.items()))

        if cache_key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[cache_key] = func(*args, **kwargs)
        return cached_results[cache_key]
    return wrapper

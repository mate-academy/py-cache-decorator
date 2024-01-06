import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    functools.wraps
    cached_results = {}

    def wrapper(*args, **kwargs) -> None:
        cache_key = (func.__name__, args, frozenset(kwargs.items()))

        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        print("Calculating new result")
        cached_results[cache_key] = func(*args, **kwargs)
        return cached_results[cache_key]
    return wrapper

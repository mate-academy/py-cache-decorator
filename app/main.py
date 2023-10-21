from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result
        print("Calculating new result")
        return result
    return wrapper

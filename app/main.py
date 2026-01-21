from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper

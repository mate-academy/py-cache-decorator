from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    stored_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in stored_results:
            print("Getting from cache")
            return stored_results[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_results[cache_key] = result
            return result

    return wrapper

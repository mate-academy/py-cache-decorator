from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    cached_results = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> any:
        cache_key = func.__name__, args, tuple(kwargs.items())

        if cache_key not in cached_results:
            cached_results[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
            return cached_results[cache_key]

        print("Getting from cache")
        return cached_results[cache_key]

    return inner

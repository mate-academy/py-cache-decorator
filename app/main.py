from __future__ import annotations
import functools


def cache(func: callable) -> None:
    cache_data = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> func:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result

    return wrapper

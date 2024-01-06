from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> dict:
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

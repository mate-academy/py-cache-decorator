from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())

        if key not in cache_store:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_store[key]

    return inner

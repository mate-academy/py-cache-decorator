from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_store:
            cache_store[key] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_store[key]
        else:
            print("Getting from cache")
            return cache_store[key]
    return wrapper

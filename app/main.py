from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_store:
            res = func(*args, **kwargs)
            cache_store[key] = res
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return cache_store[key]
    return wrapper

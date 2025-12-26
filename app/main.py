from typing import Callable, Any
import functools


def cache(func: Callable) -> Any:
    cache_data = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]
        else:
            print("Calculating new result")
            cache_data[key] = func(*args, **kwargs)
            return cache_data[key]
    return wrapper

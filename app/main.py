from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]

    return inner

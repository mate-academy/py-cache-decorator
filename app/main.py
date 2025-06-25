from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cached_data:
            print("Getting from cache")
            return cached_data[key]
        else:
            print("Calculating new result")
            cached_data[key] = func(*args, **kwargs)
            return cached_data[key]
    return wrapper

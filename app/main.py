from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_box = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        keys = (args, tuple(sorted(kwargs.items())))
        if keys in cache_box:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_box[keys] = func(*args, **kwargs)
        return cache_box[keys]
    return wrapper

from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_list = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache_list:
            print("Calculating new result")
            cache_list[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_list[key]

    return wrapper

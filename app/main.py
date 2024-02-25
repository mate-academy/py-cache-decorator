import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = args + tuple(kwargs.items())
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
            return cache_dict[key]

    return wrapper

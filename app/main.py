from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))

        if cache_dict.get(key) is not None:
            print("Getting from cache")
        else:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_dict[key]

    return wrapper

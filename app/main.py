import functools
from typing import Callable, Tuple


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def make_key(args: Tuple, kwargs: dict) -> Tuple:
        kwargs_key = tuple(sorted(kwargs.items()))
        return args + kwargs_key

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = make_key(args, kwargs)

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper

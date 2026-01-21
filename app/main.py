import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    saved_cache = dict()

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))
        if key in saved_cache:
            print("Getting from cache")
            return saved_cache[key]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            saved_cache[key] = result
            return result
    return wrapper

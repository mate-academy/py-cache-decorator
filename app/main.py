from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    _cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in _cache:
            print("Getting from cache")
            return _cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cache[key] = result
            return result
    return wrapper

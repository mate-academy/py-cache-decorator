import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in wrapper.cache:
            print("Getting from cache")
            return wrapper.cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            wrapper.cache[key] = result
            return result

    wrapper.cache = {}
    return wrapper

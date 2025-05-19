from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_result:
            print("Getting from cache")
            return cached_result[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_result[key] = result
            return result

    return wrapper

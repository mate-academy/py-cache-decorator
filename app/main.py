from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            print("Calculating new result")
            return result

    return wrapper

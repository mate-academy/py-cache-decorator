from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
        else:
            print("Getting from cache")
            result = cached_results[key]
        return result

    return wrapper

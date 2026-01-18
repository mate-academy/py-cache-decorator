from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cached_results[key]

    return wrapper

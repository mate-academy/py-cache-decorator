from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(kwargs.items())
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result
            return result

    return wrapper

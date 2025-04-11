from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_results = {}

    @wraps(func)
    def wrapper(*args) -> str:

        key = args

        if key in cache_results:
            print("Getting from cache")
            return cache_results[key]
        print("Calculating new result")
        result = func(*args)
        cache_results[key] = result
        return result

    return wrapper

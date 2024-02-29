from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def inner(*args: list) -> list:
        key = args
        if key not in cached_results:
            cached_results[key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_results[key]
    return inner

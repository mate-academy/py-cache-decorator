from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_history = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in cache_history:
            print("Getting from cache")
            return cache_history[args]
        else:
            print("Calculating new result")
            cache_history[args] = func(*args)
            return cache_history[args]
    return wrapper

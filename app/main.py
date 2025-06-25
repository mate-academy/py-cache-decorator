from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        else:
            print("Calculating new result")
            cached_data[args] = func(*args, **kwargs)
            return cached_data[args]
    return wrapper

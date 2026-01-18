from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_info = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_info:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cache_info[key] = func(*args, **kwargs)
        return cache_info[key]
    return wrapper

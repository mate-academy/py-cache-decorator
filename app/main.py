from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @wraps(func)
    def wrapper(*args) -> Any:
        key = (func.__name__, args)
        if key not in cache_dict:
            cache_dict[key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[key]

    return wrapper

import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if (func.__name__, args) in cache_store:
            print("Getting from cache")
            result = cache_store[(func.__name__, args)]
        else:
            result = func(*args)
            cache_store[(func.__name__, args)] = result
            print("Calculating new result")
        return result
    return wrapper

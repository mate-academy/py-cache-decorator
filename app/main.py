from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def inner(*args: Any) -> Any:
        if (func.__name__, args) in cache_storage:
            print("Getting from cache")
            result = cache_storage[(func.__name__, args)]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[(func.__name__, args)] = result
        return result
    return inner

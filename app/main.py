from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            result = func(*args, **kwargs)
            cache_storage[key] = result
            print("Calculating new result")
            return result

    return wrapper

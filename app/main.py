import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache_storage:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_storage[key]
    return inner

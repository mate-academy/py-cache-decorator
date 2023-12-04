from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_memory = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())
        if key in cache_memory:
            print("Getting from cache")
        else:
            cache_memory[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_memory[key]
    return inner

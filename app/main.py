from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[cache_key] = result
        return result

    return wrapper

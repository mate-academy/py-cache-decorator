from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        cache_key = (args, tuple(kwargs.items()))
        if cache_key not in storage:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[cache_key] = result
            return result
        print("Getting from cache")
        return storage[cache_key]
    return wrapper

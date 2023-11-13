from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> None:
    cache_memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cache_memory:
            print("Getting from cache")
            return cache_memory[cache_key]
        else:
            result = func(*args, **kwargs)
            cache_memory[cache_key] = result
            print("Calculating new result")
            return result
    return wrapper

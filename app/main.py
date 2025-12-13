from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> None:
    cache_memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cache_memory:
            print("Getting from cache")
        else:
            cache_memory[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_memory[cache_key]
    return wrapper

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_memory = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache_memory:
            cache_memory[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_memory[args]

    return wrapper

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_memory = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cache_memory:
            print("Getting from cache")
            return cache_memory[args]

        print("Calculating new result")
        result = func(*args)
        cache_memory[args] = result
        return result
    return wrapper

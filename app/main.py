from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    functools.wraps(func)
    cache_memory = {}

    def wrapper(*args) -> Any:
        if args not in cache_memory:
            cache_memory[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_memory[args]

    return wrapper

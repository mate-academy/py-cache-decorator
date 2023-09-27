from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def wrapper_cache(*args) -> Any:
        key = args
        if key not in memory:
            memory[key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return memory[key]

    return wrapper_cache

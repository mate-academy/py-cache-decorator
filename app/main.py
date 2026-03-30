from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args: tuple) -> Any:
        if args in cache_memory:
            print("Getting from cache")
            return cache_memory[args]

        result = func(*args)
        cache_memory[args] = result
        print("Calculating new result")
        return result
    return inner

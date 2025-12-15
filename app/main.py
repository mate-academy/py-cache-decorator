from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args) -> Any:
        if args not in cache_memory:
            print("Calculating new result")
            cache_memory[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_memory[args]

    return inner

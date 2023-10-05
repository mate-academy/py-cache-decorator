from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def wrapper(*args) -> dict:
        if args not in cache_memory:
            cache_memory[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_memory[args]

    return wrapper

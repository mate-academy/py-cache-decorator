from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def wrapper(*args) -> Any:
        if args in cache_memory:
            print("Getting from cache")
            return cache_memory[args]
        print("Calculating new result")
        result = func(*args)
        cache_memory[args] = result
        return result
    return wrapper

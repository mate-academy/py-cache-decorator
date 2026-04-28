from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: object) -> object:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result
    return wrapper

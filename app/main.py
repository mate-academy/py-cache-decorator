from typing import Callable


def cache(func: Callable) -> Callable:
    storage_cache = {}

    def wrapper(*args) -> any:

        if args in storage_cache:
            print("Getting from cache")
            return storage_cache[args]
        else:
            storage_cache[args] = func(*args)
            print("Calculating new result")
            return storage_cache[args]
    return wrapper

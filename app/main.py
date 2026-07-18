from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Callable:
        if args in cache_storage.keys():
            print("Getting from cache")
        else:
            cache_storage[args] = func(*args)
            print("Calculating new result")
        return cache_storage[args]
    return wrapper

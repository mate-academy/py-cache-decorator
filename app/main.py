from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args):
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        print("Calculating new result")
        cache_storage[args] = func(*args)
        return cache_storage[args]
    return wrapper

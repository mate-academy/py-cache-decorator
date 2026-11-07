from typing import Callable


def cache(func: Callable) -> Callable:

    cache_stored = {}

    def wrapper(*args) -> Callable:
        if args not in cache:
            cache_stored[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache[args]
    return wrapper

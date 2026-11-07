from typing import Callable


def cache(func: Callable) -> Callable:
    cache_stored = {}

    def wrapper(*args) -> Callable:
        if args not in cache_stored:
            cache_stored[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_stored[args]
    return wrapper

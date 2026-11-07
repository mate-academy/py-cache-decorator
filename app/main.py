from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}
    def wrapper(*args) -> Callable:

        if args not in cache:
            cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache[args]
    return wrapper

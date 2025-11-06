from typing import Callable


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args) -> Callable:
        if args not in saved_cache:
            saved_cache.update({args : func(*args)})
            print("Calculating new result")
            return saved_cache[args]
        else:
            print("Getting from cache")
            return saved_cache[args]
    return wrapper

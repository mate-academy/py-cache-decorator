from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def wrapper(*args) -> dict:
        if args in stored_cache:
            print("Getting from cache")
            return stored_cache[args]
        print("Calculating new result")
        stored_cache[args] = func(*args)

    return wrapper

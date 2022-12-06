from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def wrapper(*args) -> dict:
        if args in stored_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            stored_cache[args] = result
        return stored_cache[args]

    return wrapper

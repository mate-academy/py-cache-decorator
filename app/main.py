from typing import Callable


def cache(func: Callable) -> Callable:
    stored_caches = {}

    def wrapper(*args) -> dict:
        if args in stored_caches:
            print("Getting from cache")
            return stored_caches[args]
        print("Calculating new result")
        result = func(*args)
        stored_caches[args] = result
        return result
    return wrapper

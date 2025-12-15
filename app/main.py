from typing import Callable


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args) -> Callable:
        if args not in saved_cache:
            result = func(*args)
            saved_cache[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")

        return saved_cache[args]
    return wrapper

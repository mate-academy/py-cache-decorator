from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args) -> dict:

        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            result = func(*args)
            cache_store[args] = result
            print("Calculating new result")
            return result

    return wrapper

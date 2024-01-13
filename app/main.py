from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args) -> int:
        # Use args as the key for caching
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result

    return wrapper

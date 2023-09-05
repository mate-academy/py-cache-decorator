from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Any:
        if args not in cache_storage.keys():
            print("Calculating new result")
            cache_storage[*args] = func(*args)
        else:
            print("Getting from cache")

        return cache_storage[*args]
    return wrapper

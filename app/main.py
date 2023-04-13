from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_store = {}

    def inner(*args) -> Any:
        if args in cache_store:
            print("Getting from cache")
        else:
            cache_store[args] = func(*args)
            print("Calculating new result")
        return cache_store[args]

    return inner

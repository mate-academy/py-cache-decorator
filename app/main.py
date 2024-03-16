from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args) -> Any:
        nonlocal cache_store
        if args not in cache_store:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result
        else:
            print("Getting from cache")
        return cache_store[args]
    return inner

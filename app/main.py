from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage_cache = {}

    def inner(*args) -> Any:
        if args in storage_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage_cache[args] = func(*args)
        return storage_cache[args]
    return inner

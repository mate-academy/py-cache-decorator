from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_store:
            print("Calculating new result")
            cache_store[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_store[args]

    return wrapper

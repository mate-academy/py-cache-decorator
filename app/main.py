from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key not in cache_store:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_store[key]

    return wrapper

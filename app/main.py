from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        data = (func.__name__, args, tuple(kwargs.items()))
        if data not in cache_store:
            print("Calculating new result")
            cache_store[data] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_store[data]

    return wrapper

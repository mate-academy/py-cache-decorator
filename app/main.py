from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> dict:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
        else:
            cache_storage[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_storage[key]
    return wrapper

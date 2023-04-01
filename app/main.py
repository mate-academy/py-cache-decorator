from typing import Callable


def cache(func: Callable) -> Callable:

    cache_storage = {}

    def wrapper(*args, **kwargs) -> any:
        key = (func, args, frozenset(kwargs.items()))
        if key not in cache_storage:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
        else:
            print("Getting from cache")

        return cache_storage[key]

    return wrapper

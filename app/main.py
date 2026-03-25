from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args, **kwargs) -> any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)
        return cache_storage[key]
    return inner

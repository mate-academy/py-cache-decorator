from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache_storage:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_storage[key]
    return wrapper

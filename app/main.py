from typing import Callable


def cache(func: Callable) -> Callable:
    cache_1 = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_1:
            print("Getting from cache")
            return cache_1[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_1[key] = result
            return result
    return wrapper

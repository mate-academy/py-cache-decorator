from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

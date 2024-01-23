from typing import Callable


def cache(func: Callable) -> Callable:
    cache2 = {}

    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key in cache2:
            print("Getting from cache")
            return cache2[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache2[key] = result
            return result

    return wrapper

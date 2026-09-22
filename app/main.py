from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args , tuple(sorted(kwargs.items())))
        if key in caches:
            print("Getting from cache")
            return caches[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            caches[key] = result
            return result
    return wrapper

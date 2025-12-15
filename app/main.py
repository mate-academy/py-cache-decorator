from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def wrapper(*args) -> Callable:
        if args in caches:
            print("Getting from cache")
            return caches[args]
        else:
            print("Calculating new result")
            result = func(*args)
            caches[args] = result
            return result
    return wrapper

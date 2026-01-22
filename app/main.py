from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def inner(*args) -> dict:
        if args in caches:
            print("Getting from cache")
            return caches[args]
        else:
            print("Calculating new result")
            caches[args] = func(*args)
            return caches[args]
    return inner

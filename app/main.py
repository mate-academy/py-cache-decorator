from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def inner(*args) -> int:
        if args in caches:
            print("Getting from cache")
        else:
            caches[args] = func(*args)
            print("Calculating new result")
        return caches[args]

    return inner

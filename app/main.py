from typing import Callable


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def inner(*args) -> any:
        if args in saved_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_cache[args] = func(*args)
        return saved_cache[args]
    return inner

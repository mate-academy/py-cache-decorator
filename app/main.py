from typing import Callable


def cache(func: Callable) -> None:
    cache = {}

    def inner(*args) -> None:
        if args not in cache:
            print("Calculating new result")
            cache[args] = func(*args)
        else:
            print("Getting from cache")
        return cache[args]
    return inner

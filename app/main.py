from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args) -> Any:
        if args not in cache:
            print("Calculating new result")
            cache[args] = func(*args)
        else:
            print("Getting from cache")
        return cache[args]

    return inner

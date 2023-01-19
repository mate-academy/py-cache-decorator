from typing import Callable, Any


def cache(func: Callable) -> Any:
    cached = {}

    def inner(*args) -> Any:
        if args in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[args] = func(*args)
        return cached[args]

    return inner

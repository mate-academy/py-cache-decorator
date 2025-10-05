from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in cached:
            print("Calculating new result")
            cached[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cached[args]
    return inner

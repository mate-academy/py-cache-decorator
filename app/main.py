from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cached:
            print("Calculating new result")
            cached[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cached[key]
    return inner

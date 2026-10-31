from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(kwargs.items()))

        if key in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[key] = func(*args, **kwargs)

        return cached[key]
    return wrapper

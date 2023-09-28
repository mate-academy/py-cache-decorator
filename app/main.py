from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args) -> None:
        key = args
        if key in cached:
            print("Getting from cache")
            return cached[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cached[key] = result
            return result
    return wrapper

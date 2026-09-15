from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args) -> int:
        if args in cached:
            print("Getting from cache")
            return cached[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached[args] = result
            return result

    return wrapper

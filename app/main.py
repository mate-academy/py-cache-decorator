from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args: Any) -> int:
        if args not in cached:
            print("Calculating new result")
            result = func(*args)
            cached[args] = result
            return result
        else:
            print("Getting from cache")
            return cached[args]

    return inner

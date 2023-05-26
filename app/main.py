from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args) -> Any:
        if args not in cached:
            cached[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached[args]
    return inner

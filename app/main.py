from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args) -> Any:
        if args in cached.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            cached[args] = result

        return cached[args]

    return inner

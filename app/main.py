from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args: Any) -> Any:
        if args not in cached.keys():
            print("Calculating new result")
            cached[args] = func(*args)
            return cached[args]
        else:
            print("Getting from cache")
            return cached[args]

    return inner

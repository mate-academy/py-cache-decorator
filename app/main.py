from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_calcs = {}

    def wrapper(*args) -> Any:
        if args not in cached_calcs:
            print("Calculating new result")
            cached_calcs[args] = func(*args)
            return cached_calcs[args]
        else:
            print("Getting from cache")
            return cached_calcs[args]

    return wrapper

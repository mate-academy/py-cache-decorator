from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> Any:
        if args in cache:
            print("Getting from cache")
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating new result")
        return cache[args]

    return wrapper

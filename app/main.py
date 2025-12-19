from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> Any:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            res = func(*args)
        cache[args] = res
        return res
    return wrapper

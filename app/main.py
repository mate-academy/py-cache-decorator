from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> None:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        print("Calculating new result")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> Callable:
        key = args
        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache[key] = result
            return result
    return wrapper

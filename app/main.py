from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args) -> Callable:
        if args in cached_result:
            print("Getting from cache")
            return cached_result[args]
        else:
            result = func(*args)
            cached_result[args] = result
            print("Calculating new result")
            return result
    return wrapper

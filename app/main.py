from typing import Callable


def cache(func: Callable) -> Callable:

    cache_result = {}

    def wrapper(*args) -> Callable:

        if args in cache_result.keys():
            print("Getting from cache")
        else:
            cache_result[args] = func(*args)
            print("Calculating new result")
        return cache_result[args]
    return wrapper

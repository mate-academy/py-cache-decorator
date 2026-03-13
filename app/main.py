from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args) -> None:
        if args in cache_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_result[args] = func(*args)
        return cache_result[args]
    return wrapper

from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args, **kwargs) -> Callable:

        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        else:
            print("Calculating new result")
            cache_result[args] = func(*args, **kwargs)
            return cache_result[args]

    return wrapper

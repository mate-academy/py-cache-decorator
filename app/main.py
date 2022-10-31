from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args) -> Callable:
        if args not in cache_dict:
            result = func(*args)
            print("Calculating new result")
            cache_dict[args] = result
            return result
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper

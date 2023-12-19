from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> int:
        if args not in cache_dict.keys():
            result = func(*args)
            cache_dict[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper

from typing import Callable


def cache(func: Callable) -> int:
    cache_dict = {}

    def wrapper(*args) -> int:
        if args not in cache_dict.keys():
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
        else:
            print("Getting from cache")

        return cache_dict[args]
    return wrapper

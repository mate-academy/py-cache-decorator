from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args) -> int:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        else:
            result = func(*args)
            cache_dict[args] = result
            print("Calculating new result")
            return result

    return wrapper

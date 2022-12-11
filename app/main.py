from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> Callable:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        result = func(*args)
        cache_dict[args] = result
        print("Calculating new result")
        return result

    return inner

from typing import Callable


def cache(func: Callable) -> Callable:

    dict_cache = {}

    def inner(*args) -> Callable:
        if args not in dict_cache:
            dict_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return dict_cache[args]

    return inner

from typing import Callable


def cache(func: Callable) -> Callable:

    cached_dict = dict()

    def inner(*args) -> Callable:
        if args in cached_dict.keys():
            print("Getting from cache")
            return cached_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_dict[args] = result
            return result
    return inner

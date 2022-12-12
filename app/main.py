from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> None:
        if args in cache_dict.keys():
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        return cache_dict[args]
    return inner

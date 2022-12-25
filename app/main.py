from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> int:
        if args not in cache_dict:
            cache_dict.update({args: func(*args)})
            print("Calculating new result")

        else:
            print("Getting from cache")

        return cache_dict[args]

    return inner

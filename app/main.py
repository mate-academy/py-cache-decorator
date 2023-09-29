from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> [list, int]:

        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        print("Calculating new result")
        cache_dict[args] = func(*args, **kwargs)

        return cache_dict[args]

    return inner

from typing import Callable


def cache(func: Callable) -> Callable:
    cache_res = {}

    def inner(*args: Callable) -> Callable:
        if args not in cache_res:
            cache_res[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_res[args]
    return inner

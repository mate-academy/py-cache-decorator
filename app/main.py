from typing import Callable


def cache(func: Callable) -> int:
    cache_result = dict()

    def inner(*args) -> Callable:
        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        else:
            print("Calculating new result")
            cache_result[args] = func(*args)
            return cache_result[args]
    return inner

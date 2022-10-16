from typing import Callable


def cache(func: Callable) -> Callable:
    cache_1 = {}

    def inner(*args) -> Callable:
        if (func.__name__, args,) in cache_1:
            print("Getting from cache")
            return cache_1[(func.__name__, args,)]
        print("Calculating new result")
        result = func(*args)
        cache_1[func.__name__, args] = result
        return result
    return inner

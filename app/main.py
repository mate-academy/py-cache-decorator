from typing import Callable


def cache(func: Callable) -> Callable:
    dt_cache = {}

    def inner(*args) -> Callable:
        if args in dt_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dt_cache[args] = func(*args)
        return dt_cache[args]
    return inner

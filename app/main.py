from typing import Callable


def cache(func: Callable) -> Callable:
    arh_cache = {}

    def inner(*args, **kwargs) -> Callable:
        if args in arh_cache:
            print("Getting from cache")
            return arh_cache[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            arh_cache[args] = result
            return result
    return inner

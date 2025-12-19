from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> int:
        if args in cache.keys():
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
        cache[args] = res
        return res
    return wrapper

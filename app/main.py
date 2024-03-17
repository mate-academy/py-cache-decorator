from typing import Callable


def cache(func: Callable) -> Callable:
    cache_res = {}

    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))

        if key in cache_res:
            print("Getting from cache")
            return cache_res[key]

        print("Calculating new result")
        res = func(*args, **kwargs)
        cache_res[key] = res
        return res

    return inner

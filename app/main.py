from typing import Callable


def cache(func: Callable) -> Callable:

    cache_data = {}

    def inner(*arg, **kwarg) -> Callable:
        nonlocal cache_data
        if arg in list(cache_data.keys()):
            print("Getting from cache")
            return cache_data[arg]
        else:
            cache_data[arg] = func(*arg, **kwarg)
            print("Calculating new result")
            return cache_data[arg]
    return inner

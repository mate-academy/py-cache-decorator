from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*arg, **kwarg) -> Callable:
        if arg in cache_data:
            print("Getting from cache")
            return cache_data[arg]

        cache_data[arg] = func(*arg, **kwarg)
        print("Calculating new result")
        return cache_data[arg]
    return inner

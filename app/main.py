from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args, **kwargs)
        return cache_data[args]
    return inner

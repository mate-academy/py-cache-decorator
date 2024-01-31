from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args, **kwargs) -> Callable:
        params = (args, frozenset(kwargs))
        if params in cache_data:
            print("Getting from cache")
            return cache_data[params]
        else:
            cache_data[params] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_data[params]

    return inner

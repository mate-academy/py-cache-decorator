from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def inner(*args, **kwargs) -> Callable:

        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_dict[key]
    return inner

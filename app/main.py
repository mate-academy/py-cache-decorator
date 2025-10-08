from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args: None, **kwargs: None) -> Callable:
        if (args, tuple(kwargs.items())) not in cache_data:
            cache_data[(args, tuple(kwargs.items()))] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_data[(args, tuple(kwargs.items()))]
        else:
            print("Getting from cache")
            return cache_data[(args, tuple(kwargs.items()))]

    return wrapper

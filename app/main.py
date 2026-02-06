from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        keys = args + kwargs_tuple
        if keys in cache_dict:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cache_dict[keys] = func(*args, **kwargs)
        return cache_dict[keys]
    return wrapper

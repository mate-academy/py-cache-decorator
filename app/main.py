from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    def wrapper(*args, **kwargs) -> Callable:
        parameters = args
        if parameters in cache_dict:
            print("Getting from cache")
            return cache_dict[parameters]
        if parameters not in cache_dict:
            print("Calculating new result")
            cache_dict[parameters] = func(*args, **kwargs)
            return cache_dict[parameters]
    return wrapper

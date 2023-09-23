from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        if (cache_dict.get((args, func.__name__), False)
                or cache_dict.get((args, func.__name__)) == 0):

            print("Getting from cache")
            return cache_dict.get((args, func.__name__))
        else:
            print("Calculating new result")
            cache_dict[(args, func.__name__)] = func(*args, **kwargs)
            return cache_dict[(args, func.__name__)]

    return wrapper

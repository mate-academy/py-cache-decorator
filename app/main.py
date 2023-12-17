from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @functools.wraps(func)
    def cache_wrapper(*args, **kwargs) -> Callable:
        func_args = args + tuple(kwargs.values())

        if func_args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[func_args] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_dict[func_args]

    return cache_wrapper

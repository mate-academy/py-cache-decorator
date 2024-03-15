from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached_res = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        call = (id(func), args, tuple(kwargs.items()))
        if call in cached_res:
            print("Getting from cache")
            return cached_res[call]
        cached_res[call] = func(*args, **kwargs)
        print("Calculating new result")
        return cached_res[call]
    return inner

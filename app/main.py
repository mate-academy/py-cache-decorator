from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs) -> dict:
        key = args + tuple(kwargs.items()), func
        if key not in inner.cache:
            inner.cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return inner.cache[key]
    inner.cache = dict()
    return inner

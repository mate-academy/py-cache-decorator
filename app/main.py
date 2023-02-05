import functools
from typing import Callable


def cache(func: Callable) -> int:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args: int) -> int:
        nonlocal cache_store
        if args in cache_store:
            print("Getting from cache")
        else:
            cache_store[args] = func(*args)
            print("Calculating new result")
        return cache_store[args]
    return inner

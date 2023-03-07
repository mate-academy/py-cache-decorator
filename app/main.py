import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args: Any) -> Any:
        if args in cache_store:
            print("Getting from cache")
        else:
            cache_store[args] = func(*args)
            print("Calculating new result")
        return cache_store[args]
    return inner

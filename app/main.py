from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        cache_store
        if args not in cache_store:
            print("Calculating new result")
            cache_store[args] = func(*args, **kwargs)
            return cache_store[args]
        else:
            print("Getting from cache")
        return cache_store[args]
    return inner

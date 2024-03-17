from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        if args and args not in cache_store:
            print("Calculating new result")
            cache_store[args] = func(*args)
            return cache_store[args]
        elif kwargs and kwargs not in cache_store:
            print("Calculating new result")
            cache_store[kwargs] = func(*args)
            return cache_store[kwargs]
        elif args:
            print("Getting from cache")
            return cache_store[args]
        elif kwargs:
            print("Getting from cache")
            return cache_store[kwargs]
    return inner

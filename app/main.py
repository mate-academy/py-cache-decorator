from typing import Callable
import functools

cache_store = {}


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (func, args, tuple(sorted(kwargs.items())))
        if key in cache_store:
            print("Getting from cache")
            result = cache_store.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[key] = result
        return result
    return wrapper

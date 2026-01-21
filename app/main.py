from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        sorted_kwargs = tuple(sorted(kwargs.items()))
        key = (args, sorted_kwargs)
        if key in cache_store:
            result = cache_store[key]
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            cache_store[key] = result
            print("Calculating new result")
        return result
    return inner

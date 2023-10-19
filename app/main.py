from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        cache_key = args + tuple(kwargs.items())
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        print("Calculating new result")
        return result

    return wrapper

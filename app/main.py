from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        result = cache_dict.get(key, None)

        if result is not None:
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")

        return result

    return wrapper

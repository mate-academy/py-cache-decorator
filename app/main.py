from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = (frozenset(args), frozenset(kwargs.items()))
        if key not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
        else:
            print("Getting from cache")
            result = cache_dict[key]
        return result

    return wrapper

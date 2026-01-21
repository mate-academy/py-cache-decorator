from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key not in cache_dict:
            print("Calculating new result")
            cache_dict[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[cache_key]

    return wrapper

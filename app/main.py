from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result

        return result

    return wrapper

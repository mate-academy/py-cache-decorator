from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = args
        if cache_dict.get(key) is not None:
            print("Getting from cache")
        else:
            cache_dict[key] = func(*args)
            print("Calculating new result")

        return cache_dict[key]

    return wrapper

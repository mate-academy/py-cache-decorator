from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:

        if func not in cache_dict:
            cache_dict[func] = {}

        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_dict[func]:
            print("Getting from cache")
            return cache_dict[func][key]
        else:
            result = func(*args, **kwargs)
            cache_dict[func][key] = result
            print("Calculating new result")
            return cache_dict[func][key]

    return inner

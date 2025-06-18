from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}  # variable for cache

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        # if we have a hashed value for this call, then we return it
        cache_key = (args, frozenset(sorted(kwargs.items())))
        if cache_key in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[cache_key] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_dict[cache_key]

    return inner

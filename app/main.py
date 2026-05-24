from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args: tuple, **kwargs: dict) -> Any:
        data = args, tuple(kwargs.items())
        if data not in cache_dict:
            print("Calculating new result")
            cache_dict[data] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[data]
    return inner

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[key]
    return wrapper

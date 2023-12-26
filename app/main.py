from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_key = func.__name__
        key = (func_key, args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        print("Calculating new result")
        return result

    return wrapper

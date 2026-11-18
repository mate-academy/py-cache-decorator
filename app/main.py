from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        func_result = func(*args, **kwargs)
        cache_dict[key] = func_result
        print("Calculating new result")
        return func_result
    return wrapper

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        nonlocal cache_dict

        func_name = func.__name__
        if func_name not in cache_dict:
            cache_dict[func_name] = {}

        if args in cache_dict[func_name]:
            print("Getting from cache")
        else:
            cache_dict[func_name][args] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_dict[func_name][args]

    return inner

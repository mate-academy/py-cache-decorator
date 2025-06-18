from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}  # variable for simple cache

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        nonlocal cache_dict

        func_name = func.__name__  # save function name in variable
        # if a function is called for the first time,
        # then we create a new place for it
        if func_name not in cache_dict:
            cache_dict[func_name] = {}

        # if we have a hashed value for the function, then we return it
        cache_key = (args, frozenset(sorted(kwargs.items())))
        if cache_key in cache_dict[func_name]:
            print("Getting from cache")
        else:
            cache_dict[func_name][cache_key] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_dict[func_name][cache_key]

    return inner

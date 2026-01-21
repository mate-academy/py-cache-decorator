from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    # the key is a tuple of arguments, and a value is the expression result
    cached_args = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_args:
            print("Getting from cache")
            res = cached_args[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cached_args[key] = res

        return res

    return wrapper

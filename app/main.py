from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    result_func_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = (func, args, tuple(sorted(kwargs.items())))
        if key in result_func_dict:
            print("Getting from cache")
        else:
            result_func_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        return result_func_dict[key]
    return wrapper

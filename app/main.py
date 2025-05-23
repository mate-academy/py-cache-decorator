from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key_result = (args, tuple(sorted(kwargs.items())))
        if key_result in result:
            print("Getting from cache")
        else:
            result[key_result] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key_result]
    return wrapper

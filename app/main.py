from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        key = (args, frozenset(kwargs.items()))
        if key not in result:
            print("Calculating new result")
            new_result = func(*args, **kwargs)
            result[key] = new_result
        else:
            print("Getting from cache")
            return result[key]
        return new_result
    return wrapper

from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        key = (args, frozenset(kwargs.items()))
        if key not in result:
            print("Calculating new result")
            result[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return result[key]
    return wrapper

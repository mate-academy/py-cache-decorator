from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    completed = {}

    @wraps(func)
    def wrapper(*args) -> callable:
        if args in completed:
            print("Getting from cache")
            return completed[args]
        else:
            result = func(*args)
            completed[args] = result
            print("Calculating new result")
            return result

    return wrapper

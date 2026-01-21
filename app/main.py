from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in result:
            print("Getting from cache")
            return result[args]

        print("Calculating new result")
        result[args] = func(*args)
        return result[args]

    return wrapper

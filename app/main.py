from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = dict()

    @wraps(func)
    def wrapper(*args) -> any:
        result = cached_data.get(args)
        if result is None:
            print("Calculating new result")
            result = func(*args)
            cached_data[args] = result
        else:
            print("Getting from cache")
        return result

    return wrapper

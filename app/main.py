from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        key = args

        if key in result_dict:
            print("Getting from cache")
        else:
            result_dict[key] = func(*args)
            print("Calculating new result")

        return result_dict[key]

    return wrapper

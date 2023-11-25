from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_of_functions = {}

    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in dict_of_functions:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_of_functions[key] = func(*args, **kwargs)

        return dict_of_functions[key]

    return wrapper

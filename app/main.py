from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_functions = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if (func.__name__, args) not in cached_functions:
            result = func(*args)
            cached_functions[(func.__name__, args)] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cached_functions.get((func.__name__, args), "Error")
    return wrapper

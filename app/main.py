from typing import Callable
from functools import wraps
from functools import wraps

def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> wraps:

        key = (func.__name__, args)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args)
        cache_dict[key] = result
        return result

    return wrapper

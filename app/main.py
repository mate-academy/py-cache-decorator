from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        arguments = args + tuple(kwargs.items())
        if arguments not in cache_result:
            print("Calculating new result")
            cache_result[arguments] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_result[arguments]

    return wrapper

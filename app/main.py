from typing import Callable
from functools import wraps

cache_obj = {}


def cache(func: Callable) -> Callable:
    cache_obj = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        if func.__name__ not in cache_obj:
            cache_obj[func.__name__] = {}

        if args not in cache_obj[func.__name__]:
            cache_obj[func.__name__][args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_obj[func.__name__][args]

    return wrapper

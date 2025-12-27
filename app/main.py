from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        if args in cache:
            print("Getting from cache")
            return cache[args][str(func.__name__)]
        cache[args] = {str(func.__name__): func(*args, **kwargs)}
        print("Calculating new result")
        return cache[args][str(func.__name__)]
    return inner

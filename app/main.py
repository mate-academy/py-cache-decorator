from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Any:
    cache = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = func(*args)
        return cache[args]

    return inner

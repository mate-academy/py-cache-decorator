from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_funcs = {}

    @wraps(func)
    def wrapper(*args) -> int:
        if args in cached_funcs:
            print("Getting from cache")
            return cached_funcs[args]

        print("Calculating new result")
        res = func(*args)
        cached_funcs[args] = res

        return res

    return wrapper

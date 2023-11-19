from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_funcs = {}

    @wraps(func)
    def wrapper(*args) -> int:
        for key_arg in cached_funcs:
            if args == key_arg:
                print("Getting from cache")
                return cached_funcs[args]

        print("Calculating new result")
        res = func(*args)
        cached_funcs[args] = res

        return res

    return wrapper

from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = str(id(func)) + "(" + f"{(args, frozenset(kwargs.items()))}" + ")"
        # print(key)
        if key not in cached:
            print("Calculating new result")
            cached[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cached[key]
    return wrapper

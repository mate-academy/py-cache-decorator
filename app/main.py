import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    func_chache = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in func_chache:
            print("Getting from cache")
            return func_chache[args]
        else:
            print("Calculating new result")
            func_chache[args] = func(*args)
            return func_chache[args]
    return wrapper

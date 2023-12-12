from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    func_cache = {}

    @functools.wraps(func)
    def wrapper(*args) -> any:

        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]

        print("Calculating new result")
        func_cache[args] = func(*args)
        return func_cache[args]

    return wrapper

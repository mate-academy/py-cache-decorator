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
        result = func(*args)
        func_cache[args] = result
        return result

    return wrapper

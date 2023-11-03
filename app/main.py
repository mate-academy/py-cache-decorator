from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    func_cache = {}

    @functools.wraps(func)
    def wrapper(*args) -> any:

        if args in func_cache.get(func.__name__, ()):
            print("Getting from cache")
            return func_cache[func.__name__][args]

        print("Calculating new result")
        result = func(*args)
        if func_cache.get(func.__name__):
            func_cache[func.__name__].update({args: result})
        else:
            func_cache[func.__name__] = {args: result}
            return result

    return wrapper

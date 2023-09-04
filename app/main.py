import functools
from typing import Callable
def cache(func) -> Callable:
    cached_results = {}
    functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        res = func(*args)
        cached_results[args] = res
        print("Calculating new result")
        return res

    return wrapper

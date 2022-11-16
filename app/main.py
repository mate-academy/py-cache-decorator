import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    args_results = {}

    @functools.wraps(func)
    def inner(*args) -> Callable:
        if args not in args_results:
            print("Calculating new result")
            result = func(*args)
            args_results[args] = result
        else:
            print("Getting from cache")
        return args_results[args]
    return inner

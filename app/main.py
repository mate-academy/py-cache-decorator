from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def inner(*args) -> Callable:
        if args not in cached_results:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result
        else:
            print("Getting from cache")
            result = cached_results[args]
        return result

    return inner

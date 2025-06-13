from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result_2 = func(*args)
            results[args] = result_2
            return result_2
    return wrapper

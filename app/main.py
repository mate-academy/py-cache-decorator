from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> object:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        result = func(*args)
        cached_results[args] = result

        return result

    return wrapper

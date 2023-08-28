from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    caching_result = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if args in caching_result:
            print("Getting from cache")
            return caching_result[args]

        print("Calculating new result")
        result = func(*args)
        caching_result[args] = result

        return result

    return wrapper

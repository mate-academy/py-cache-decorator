from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    saved_result = {}

    @wraps(func)
    def wrapper_cache(*args) -> dict:
        if args in saved_result:
            print("Getting from cache")
            return saved_result[args]

        print("Calculating new result")
        saved_result[args] = func(*args)
        return saved_result[args]

    return wrapper_cache

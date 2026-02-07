from typing import Callable
from functools import wraps


def cache(func : Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]

        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result

    return wrapper

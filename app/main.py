from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args) -> tuple:
        if args in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[args] = func(*args)
        return stored_results[args]

    return wrapper

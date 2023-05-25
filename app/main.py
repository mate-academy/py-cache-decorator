from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if args in results:
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        results[args] = func(*args)
        return results[args]

    return wrapper

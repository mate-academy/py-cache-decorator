from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in results:
            print("Getting from cache")
            return results[key]

        print("Calculating new result")
        results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper

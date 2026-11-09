from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper

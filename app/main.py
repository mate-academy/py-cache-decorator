from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in memo:
            print("Getting from cache")
            return memo[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memo[key] = result
            return result

    return wrapper

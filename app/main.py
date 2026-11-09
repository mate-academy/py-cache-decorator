from functools import wraps
from typing import Callable
from typing import Any as any


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: any, **kwargs: any) -> any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper

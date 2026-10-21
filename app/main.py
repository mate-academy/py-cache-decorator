from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in memo:
            print("Getting from cache")
            return memo[args]

        print("Calculating new result")
        result = func(*args)
        memo[args] = result
        return result

    return wrapper

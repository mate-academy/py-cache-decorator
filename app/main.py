
from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a unique immutable key for args and kwargs

        key = (args, frozenset(kwargs.items()))

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper

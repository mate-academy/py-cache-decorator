from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in memo:
            print("Getting from cache")
            return memo[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[cache_key] = result
        return result

    return wrapper

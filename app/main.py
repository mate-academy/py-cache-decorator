from functools import wraps
from typing import Any, Callable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items()))) if kwargs else args

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper

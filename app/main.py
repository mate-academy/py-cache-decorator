from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    data_memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in data_memo:
            print("Getting from cache")
            return data_memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        data_memo[key] = result
        return data_memo[key]

    return wrapper

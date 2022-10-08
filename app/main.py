from functools import wraps
from typing import Any


def cache(func: Any) -> Any:
    cache_result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in cache_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_result[args] = func(*args, **kwargs)
        return cache_result[args]
    return wrapper

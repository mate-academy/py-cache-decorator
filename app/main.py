from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
        return cached_results[key]

    return wrapper

from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result
        print("Calculating new result")
        return result

    return wrapper

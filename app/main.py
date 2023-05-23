from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        cached_results[key] = func(*args, **kwargs)
        print("Calculating new result")
        return cached_results[key]

    return wrapper

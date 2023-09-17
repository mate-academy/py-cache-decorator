from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()),)
        if key in cache_results:
            print("Getting from cache")
        else:
            cache_results[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_results[key]

    return wrapper

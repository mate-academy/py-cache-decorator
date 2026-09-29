from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper

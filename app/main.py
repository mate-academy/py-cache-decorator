from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = args + tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper

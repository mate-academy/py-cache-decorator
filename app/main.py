from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        # Not sure what return type annotation to use above
        key = (func.__name__, args, tuple(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper

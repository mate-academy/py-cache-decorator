from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:

    cached = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached:
            print("Getting from cache")
            return cached[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached[key] = result
            return result
    return inner

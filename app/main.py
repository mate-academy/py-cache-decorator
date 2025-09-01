from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        kwargs_key = tuple(sorted(kwargs.items()))
        key = (args, kwargs_key)

        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper

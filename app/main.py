from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args, tuple(sorted(kwargs.items()))
        if key not in cache:
            print("Calculating new result")
            cache[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache.get(key)
    return wrapper

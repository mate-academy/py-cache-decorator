from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        res = func(*args, **kwargs)
        cache[key] = res
        return res

    return wrapper

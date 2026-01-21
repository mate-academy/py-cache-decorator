from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    caches = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in caches:
            print("Calculating new result")
            result = func(*args, **kwargs)
            caches[key] = result
            return result
        else:
            print("Getting from cache")
            return caches[key]
    return inner

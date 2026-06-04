from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached = {}
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if cached.get(key, None) is None:
            cached[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached[key]
    return wrapper

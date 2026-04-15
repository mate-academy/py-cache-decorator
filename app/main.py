from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()),)
        if key not in cache_storage:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result
        else:
            print("Getting from cache")
            return cache_storage[key]
    return wrapper

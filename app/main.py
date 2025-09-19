from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = tuple([args, tuple(sorted(kwargs.items()))])
        if key in list(stored_cache.keys()):
            print("Getting from cache")
            return stored_cache[key]
        print("Calculating new result")
        stored_cache.update({key: func(*args, **kwargs)})
        return stored_cache[key]
    return wrapper

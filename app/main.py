from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Any:
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_data:
            cache_data[args] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_data[args]
        else:
            print("Getting from cache")
            return cache_data[args]

    return wrapper

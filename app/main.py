from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_data[key] = result
        return result

    return wrapper

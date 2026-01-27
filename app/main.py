from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        print("Calculating new result")
        return result
    return wrapper

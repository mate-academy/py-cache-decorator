from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        print("Calculating new result")
        return result

    return wrapper

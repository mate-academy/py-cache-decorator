from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = args + tuple(sorted(kwargs.items()))

        if cache_key in cache_data:
            print("Getting from cache")
            return cache_data[cache_key]
        else:
            result_of_run = func(*args, **kwargs)
            cache_data[cache_key] = result_of_run
            print("Calculating new result")
            return result_of_run

    return wrapper

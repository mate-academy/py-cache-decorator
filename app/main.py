from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = args + kwargs_tuple
        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[cache_key] = result
            return result
    return inner

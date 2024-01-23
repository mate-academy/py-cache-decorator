from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cached_results:
            print("Getting from cache")
        else:
            cached_results[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
        return cached_results[cache_key]
    return wrapper

from functools import wraps
from typing import Callable, Any

cache_results = {}


def make_key(args: Any, kwargs: Any) -> tuple:
    # Convert kwargs to a sorted tuple of (key, value) pairs
    kwargs_tuple = tuple(sorted(kwargs.items()))
    return (args, kwargs_tuple)


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if func not in cache_results:
            cache_results[func] = {}

        cache_key = make_key(args, kwargs)
        if cache_key not in cache_results[func]:
            print("Calculating new result")
            cache_results[func][cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_results[func][cache_key]
    return wrapper

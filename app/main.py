from functools import wraps
from typing import Callable, Any

cache_results = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if func not in cache_results:
            cache_results[func] = {}

        if args not in cache_results[func]:
            print("Calculating new result")
            cache_results[func][args] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_results[func][args]
    return wrapper

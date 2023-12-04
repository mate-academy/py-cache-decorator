from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result
            print("Calculating new result")
            return result
    return wrapper

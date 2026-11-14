from typing import Any
from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = tuple(sorted((args, *kwargs.items())))
        if (key in results_cache):
            print("Getting from cache")
            return results_cache.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result
            return result
    return wrapper

from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        result = cached_results.get(key, None)

        if result is None:
            result = func(*args, **kwargs)
            cached_results[key] = result
            print("Calculating new result")
        else:
            print("Getting from cache")

        return result

    return wrapper

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result
        return results[key]
    return wrapper

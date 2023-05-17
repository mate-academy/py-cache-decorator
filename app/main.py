from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return wrapper

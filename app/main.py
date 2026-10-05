from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper

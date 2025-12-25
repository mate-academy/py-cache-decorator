from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        return results[key]
    return inner

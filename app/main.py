from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper

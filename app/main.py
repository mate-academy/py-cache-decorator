from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        key = args
        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*args)
        results[key] = result
        return result
    return wrapper

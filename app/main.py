from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in results_cache:
            print("Getting from cache")
            return results_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results_cache[args] = result
            return result

    return wrapper

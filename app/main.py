from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[args] = result
        return result

    return wrapper

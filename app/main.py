from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        dict_key = (func, args, frozenset(kwargs.items()))
        if dict_key in cached_results:
            print("Getting from cache")
            return cached_results[dict_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[dict_key] = result
        return result

    return wrapper

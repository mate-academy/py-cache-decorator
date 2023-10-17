from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_result = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cached_result.keys():
            cached_result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_result[args]

    return wrapper

from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:

        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        cached_results[args] = func(*args)
        return cached_results[args]

    return wrapper

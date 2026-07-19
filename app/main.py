from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache_results:
            print("Getting from cache")
            return cache_results[args]

        print("Calculating new result")
        result = func(*args)
        cache_results[args] = result

        return result

    return wrapper
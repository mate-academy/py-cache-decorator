from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args: tuple) -> Any:
        if args in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results.update({args: func(*args)})
        return cached_results.get(args)

    return wrapper

from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)

        return results[args]

    return wrapper

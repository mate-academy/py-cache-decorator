from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:

    results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results.update({args: result})
            return result
    return wrapper

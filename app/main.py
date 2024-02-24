from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        result = func(*args)
        results[args] = result
        return result

    return wrapper

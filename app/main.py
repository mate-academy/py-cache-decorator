import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in results:
            result = func(*args)
            results[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return results[args]

    return wrapper

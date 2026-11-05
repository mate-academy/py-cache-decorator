from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        res = func(*args)
        results[args] = res
        return res

    return wrapper

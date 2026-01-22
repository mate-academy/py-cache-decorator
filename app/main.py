from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args not in results:
            results[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results[args]
    return wrapper

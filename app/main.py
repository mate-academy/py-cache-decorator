from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in stored_results:
            print("Getting from cache")
        else:
            stored_results[args] = func(*args)
            print("Calculating new result")
        return stored_results[args]
    return wrapper

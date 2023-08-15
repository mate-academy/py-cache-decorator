from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        func_name = func.__name__
        if func_name not in results:
            results[func_name] = {}
        if args in results[func_name]:
            print("Getting from cache")
            return results[func_name][args]
        else:
            print("Calculating new result")
            results[func_name][args] = func(*args)
            return results[func_name][args]
    return wrapper

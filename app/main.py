from typing import Callable
from typing import Any
from functools import wraps


def cache(func: Callable) -> Callable:
    completed_runs = {}
    @wraps(func)
    def wrapper(*args) -> Any:
        key = (func.__name__, args)
        if key not in completed_runs:
            result = func(*args)
            completed_runs[key] = result
            print("Calculating new result")
            return result
        print("Getting from cache")
        return completed_runs[key]

    return wrapper

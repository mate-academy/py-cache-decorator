from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    func_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        key = args

        if key in func_results:
            print("Getting from cache")
            return func_results[key]

        print("Calculating new result")
        result = func(*args)
        func_results[key] = result
        return result

    return wrapper

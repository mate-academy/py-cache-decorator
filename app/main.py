from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_args = (args, tuple(kwargs.items()))
        if func_args in cached_results:
            print("Getting from cache")
            return cached_results[func_args]

        print("Calculating new result")
        func_result = func(*args, **kwargs)
        cached_results[func_args] = func_result
        return func_result

    return wrapper

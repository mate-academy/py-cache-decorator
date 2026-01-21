from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in func_cache:
            print("Getting from cache")
            result = func_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[args] = result
        return result
    return wrapper

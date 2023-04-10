from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        nonlocal cached_data
        if args in cached_data.keys():
            print("Getting from cache")
            result = cached_data.get(args)
        else:
            result = func(*args)
            cached_data.update({args: result})
            print("Calculating new result")
        return result

    return wrapper

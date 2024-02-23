from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_dict = {}

    @wraps(func)
    def wrapper(*args: tuple) -> Any:
        if args in storage_dict:
            print("Getting from cache")
            return storage_dict[args]
        else:
            result = func(*args)
            storage_dict[*args] = result
            print("Calculating new result")
            return result
    return wrapper

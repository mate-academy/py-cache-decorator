from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_dict = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = args, frozenset(kwargs.items())
        if key in storage_dict:
            print("Getting from cache")
            return storage_dict[key]

        result = func(*args, **kwargs)
        storage_dict[key] = result
        print("Calculating new result")
        return result
    return wrapper

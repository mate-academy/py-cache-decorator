from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Any:
    storage_of_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in storage_of_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage_of_data[key] = func(*args, **kwargs)
        return storage_of_data[key]

    return wrapper

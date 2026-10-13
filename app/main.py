from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in stored_data:
            print("Getting from cache")
            return stored_data[args]
        print("Calculating new result")
        stored_data[args] = func(*args, **kwargs)
        return stored_data[args]
    return wrapper

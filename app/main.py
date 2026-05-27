from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_data = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in stored_data:
            print("Getting from cache")
            return stored_data[args]
        else:
            print("Calculating new result")
            stored_data[args] = func(*args)
            return stored_data[args]
    return wrapper

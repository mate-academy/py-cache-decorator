from typing import Callable
from functools import wraps


def cache(func: Callable) -> None:
    stored_values = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        if args not in stored_values:
            stored_values[args] = func(*args, **kwargs)
            print("Calculating new result")
            return stored_values[args]
        else:
            print("Getting from cache")
            return stored_values[args]
    return wrapper

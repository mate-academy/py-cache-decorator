from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    parameters = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in parameters:
            parameters[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return parameters[key]
    return wrapper

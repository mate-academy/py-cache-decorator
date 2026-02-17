from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        key = (args, tuple(sorted(kwargs.items())))
        if key in data:
            print("Getting from cache")
            result = data[key]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            data[key] = result

        return result

    return wrapper

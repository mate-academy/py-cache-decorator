from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if (args, tuple(kwargs.values())) not in data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data[(args, tuple(kwargs.values()))] = result
            return result

        print("Getting from cache")
        result = data[(args, tuple(kwargs.values()))]
        return result
    return wrapper

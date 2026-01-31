from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in data:
            print("Getting from cache")
            return data[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data[key] = result
            return result
    return wrapper

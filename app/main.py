from typing import Callable
from typing import Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cached_data.keys():
            cached_data[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_data[key]
    return wrapper

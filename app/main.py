from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        nonlocal cached_data
        if args in cached_data.keys():
            print("Getting from cache")
        else:
            cached_data[args] = func(*args)
            print("Calculating new result")
        return cached_data.get(args)

    return wrapper

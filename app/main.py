import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        key = args
        if key not in cached_data:
            print("Calculating new result")
            cached_data[key] = func(*args)
            return cached_data[key]

        print("Getting from cache")

        return cached_data[key]

    return wrapper

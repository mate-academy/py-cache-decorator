import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    repeating_data = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in repeating_data:
            print("Getting from cache")
            return repeating_data[key]
        print("Calculating new result")
        repeating_data[key] = func(*args, **kwargs)
        return repeating_data[key]
    return inner

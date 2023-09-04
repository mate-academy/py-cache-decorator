import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    repeating_data = {}

    @functools.wraps(func)
    def inner(*args) -> Any:
        if (args,) in repeating_data:
            print("Getting from cache")
            return repeating_data[(args,)]
        print("Calculating new result")
        repeating_data[(args,)] = func(*args)
        return repeating_data[(args,)]
    return inner

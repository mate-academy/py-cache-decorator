from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args: None) -> None:
        if args in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args)
        return cache_data[args]

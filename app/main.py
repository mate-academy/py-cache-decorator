from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache: dict = {}

    @wraps(func)
    def wrapper(*args: tuple) -> Any:
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = func(*args)

        return cache[args]

    return wrapper

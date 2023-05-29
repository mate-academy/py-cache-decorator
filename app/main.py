from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in cached:
            print("Getting from cache")
        else:
            cached[args] = func(*args)
            print("Calculating new result")
        return cached[args]
    return inner

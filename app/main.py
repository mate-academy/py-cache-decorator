from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result: dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> int:
        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args, **kwargs)
            print("Calculating new result")
        return result[args]
    return inner

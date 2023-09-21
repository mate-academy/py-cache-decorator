from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result: dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> int:
        if str(args) + str(kwargs.values()) not in result.keys():
            result[str(args) + str(kwargs.values())] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[str(args) + str(kwargs.values())]
    return inner

from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}  # this will be stored in closure because it is nonlocal

    @wraps(func)
    def wrapper(*args) -> list:
        keys = tuple(args)
        if keys not in storage:
            print("Calculating new result")
            storage[keys] = func(*args)
        else:
            print("Getting from cache")
        return storage[keys]

    return wrapper

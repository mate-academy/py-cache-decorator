from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}  # this will be stored in closure because it is nonlocal

    @wraps(func)
    def wrapper(*args, **kwargs) -> list:
        # Unpack args and kwargs into a tuple to be used as dict keys
        keys = (tuple(args) + tuple(kwargs.keys()))
        if keys not in storage:
            print("Calculating new result")
            storage[keys] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return storage[keys]

    return wrapper

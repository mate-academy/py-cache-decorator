from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    """
    # dict items(storage = {})
    will be stored in closure because it is nonlocal
    # keys = tuple(args) - Unpack args (and kwargs)
    into a tuple to be used as dict keys

    """
    storage = {}

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

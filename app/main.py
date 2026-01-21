from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args) -> None:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        print("Calculating new result")
        result = func(*args)
        storage[args] = result
        return result
    return wrapper

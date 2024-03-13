from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in storage:
            print("Getting from cache")
        else:
            storage[args] = func(*args)
            print("Calculating new result")

        return storage[args]

    return wrapper

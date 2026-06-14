from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        func_args = args in storage
        if func_args:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)

        return storage[args]

    return wrapper

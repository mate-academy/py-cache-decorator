from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        res = func(*args, **kwargs)
        storage[key] = res
        return res

    return wrapper

from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))

        if key in store:
            print("Getting from cache")
            return store[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper

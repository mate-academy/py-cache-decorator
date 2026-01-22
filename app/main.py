from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key not in storage:
            print("Calculating new result")
            storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return storage[key]
    return wrapper

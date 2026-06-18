from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        cache_key = (args, tuple(kwargs.items()))

        if cache_key in storage:
            print("Getting from cache")
            return storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[cache_key] = result
        return result

    return inner

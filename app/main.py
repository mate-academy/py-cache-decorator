from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs: Any) -> Any:
        kwargs_key = tuple(sorted(kwargs.items()))
        key = (args, kwargs_key)
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result
    return wrapper

import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (
            ",".join(str(arg) for arg in args)
            + ","
            + ",".join(f"{key}={value}" for key, value in kwargs.items())
        )
        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper

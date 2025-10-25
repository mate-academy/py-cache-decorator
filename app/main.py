import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple)
        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper

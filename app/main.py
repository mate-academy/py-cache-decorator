from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        try:
            hash(key)
        except TypeError:
            return func(*args, **kwargs)

        if key not in cache_data:
            print("Calculating new result")
            cache_data[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_data[key]
    return wrapper

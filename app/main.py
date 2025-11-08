from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_obj = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if len(kwargs) > 0:
            kwargs = tuple(sorted(kwargs.items()))

        if func.__name__ not in cache_obj:
            cache_obj[func.__name__] = {}
        key = str(args) + str(kwargs)

        if key not in cache_obj[func.__name__]:
            cache_obj[func.__name__][key] = func(*args, **dict(kwargs))
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_obj[func.__name__][key]

    return wrapper

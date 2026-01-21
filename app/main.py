from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        kwargs_tuple = tuple(kwargs.items())
        key = (args, kwargs_tuple)

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper

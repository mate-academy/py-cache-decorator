from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        dict_key = args + tuple(kwargs.items())
        if dict_key not in wrapper.cache:
            wrapper.cache[dict_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return wrapper.cache[dict_key]

    wrapper.cache = {}
    return wrapper

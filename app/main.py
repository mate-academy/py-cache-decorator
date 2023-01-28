from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

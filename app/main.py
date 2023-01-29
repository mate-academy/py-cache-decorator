from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Any:
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

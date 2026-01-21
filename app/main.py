from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache: Dict:[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            func_cache[cache_key] = func(*args, **kwargs)
            return func_cache[cache_key]
    return wrapper

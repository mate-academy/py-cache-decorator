from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_cache(*args) -> int:
        if args not in wrapper_cache.cache:
            print("Calculating new result")
            wrapper_cache.cache[args] = func(*args)
        else:
            print("Getting from cache")
        return wrapper_cache.cache[args]
    wrapper_cache.cache = {}
    return wrapper_cache

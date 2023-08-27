from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_cache(*args, **kwargs) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            print("Calculating new result")
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache

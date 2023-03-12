from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args: tuple, **kwargs: dict) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            print("Calculating new result")
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            return wrapper_cache.cache[cache_key]
        else:
            print("Getting from cache")
            return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache

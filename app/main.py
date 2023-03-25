import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable :
    area_cache = {}

    @functools.wraps(func)
    def wrap_cache(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())
        if key in area_cache:
            print("Getting from cache")
            return area_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            area_cache[key] = result
            return result
    return wrap_cache

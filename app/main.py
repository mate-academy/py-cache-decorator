from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sorted_items = tuple(sorted(kwargs.items()))
        key = (args, sorted_items)

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper

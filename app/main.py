from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in dict_cache:
            print("Getting from cache")
            return dict_cache[key]

        result = func(*args, **kwargs)
        dict_cache[key] = result
        print("Calculating new result")
        return result

    return wrapper

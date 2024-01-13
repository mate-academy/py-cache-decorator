from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args) -> Any:
        func_name = func.__name__
        if func_name in cache_dict and args in cache_dict[func_name]:
            print("Getting from cache")
            return cache_dict[func_name][args]
        print("Calculating new result")
        result = func(*args)
        cache_dict.setdefault(func_name, {})[args] = result
        return result

    return inner

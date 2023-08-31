from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        input_args = args
        if input_args in cache_dict:
            print("Getting from cache")
            return cache_dict[input_args]
        print("Calculating new result")
        result = func(*args)
        cache_dict[input_args] = result
        return result

    return wrapper

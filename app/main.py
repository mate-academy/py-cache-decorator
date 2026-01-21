from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    temp_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = func.__name__, *args + tuple(kwargs.keys())
        if key not in temp_dict:
            result = func(*args, **kwargs)
            temp_dict[key] = result
            print("Calculating new result")
            return result
        print("Getting from cache")
        return temp_dict[key]

    return wrapper

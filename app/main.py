from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())

        if key not in result_dict:
            print("Calculating new result")
            result_dict[key] = result_value = func(*args, **kwargs)
            return result_value

        print("Getting from cache")
        return result_dict[key]

    return wrapper

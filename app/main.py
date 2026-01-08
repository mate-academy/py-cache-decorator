from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items()))        )

        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        result_dict[key] = result
        return result

    return wrapper

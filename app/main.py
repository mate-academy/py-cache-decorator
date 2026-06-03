from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    my_dict = {}
    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in my_dict:
            print("Getting from cache")
            return my_dict[key]
        result = func(*args, **kwargs)
        my_dict[key] = result
        print("Calculating new result")
        return result

    return inner

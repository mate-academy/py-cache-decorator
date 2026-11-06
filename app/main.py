from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        input_args = (*args, tuple(sorted(kwargs.items())))
        if any(isinstance(arg, (dict, list, set, bytearray))
               for arg in input_args):
            print("Calculating new result")
            return func(*args, **kwargs)

        if input_args not in cache:
            cache[input_args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache[input_args]
    return wrapper

from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_dictionary = {}

    @wraps(func)
    def inner_function(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in storage_dictionary:
            print("Getting from cache")
        else:
            storage_dictionary[key] = func(*args, **kwargs)
            print("Calculating new result")
        return storage_dictionary[key]
    return inner_function

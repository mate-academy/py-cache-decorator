
from typing import Callable


def cache(func: Callable) -> Callable:
    data_base = {}

    def inner(*args, **kwargs) -> Callable:
        combined_arguments = (args, frozenset(kwargs.items()))
        if combined_arguments not in data_base:
            result = func(*args, **kwargs)
            data_base[combined_arguments] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
            result = data_base[combined_arguments]
        return result
    return inner

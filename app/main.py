
from typing import Callable


def cache(func: Callable) -> Callable:
    data_base = {}

    def inner(*args, **kwargs) -> Callable:
        combined_arguments = (args, frozenset(kwargs.items()))
        if combined_arguments not in data_base:
            data_base[combined_arguments] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return data_base[combined_arguments]
    return inner

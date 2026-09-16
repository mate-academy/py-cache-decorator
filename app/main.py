from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    special_dict = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in special_dict:
            print("Getting from cache")
            return special_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        special_dict[key] = result
        return result
    return inner

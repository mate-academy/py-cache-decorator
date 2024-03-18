from typing import Callable


def cache(func: Callable) -> Callable:
    closure_dict = {}

    def inner(*args, **kwargs) -> list:
        key = (args, frozenset(kwargs.items()))
        if key not in closure_dict.keys():
            result = func(*args, **kwargs)
            closure_dict[key] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return closure_dict[key]

    return inner

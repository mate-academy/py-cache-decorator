from typing import Callable


def cache(func: Callable) -> Callable:
    closure_list = {}

    def inner(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key not in closure_list.keys():
            result = func(*args, **kwargs)
            closure_list[key] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return closure_list[key]

    return inner

from typing import Callable


def cache(func: Callable) -> Callable:
    new_dict = {}

    def wrapper(*args, **kwargs) -> dict:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in new_dict:
            print("Getting from cache")
            return new_dict[key]
        result = func(*args, **kwargs)
        new_dict[key] = result
        print("Calculating new result")
        return result
    return wrapper

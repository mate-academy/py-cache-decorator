from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> int | list:
        key = (args, frozenset(kwargs.items()))
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            print("Calculating new result")
            result[key] = func(*args, **kwargs)
            return result[key]

    return wrapper

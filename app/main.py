from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key not in result:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[key]
    return wrapper

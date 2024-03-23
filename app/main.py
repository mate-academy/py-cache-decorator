from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (func.__name__, args, frozenset(kwargs))
        if key in result:
            print("Getting from cache")
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key]

    return wrapper

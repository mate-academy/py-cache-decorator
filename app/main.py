from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs))
        if key in result:
            print("Getting from cache")
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key]

    return wrapper

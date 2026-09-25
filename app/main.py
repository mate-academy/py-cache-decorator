from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
            return result[key]
    return wrapper

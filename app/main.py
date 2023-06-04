from typing import Callable, Any


def cache(func: Callable) -> Callable:
    calculation = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs))
        if key in calculation:
            print("Getting from cache")
        else:
            print("Calculating new result")
            calculation[key] = func(*args, **kwargs)
        return calculation[key]

    return wrapper

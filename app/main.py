from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in data:
            print("Getting from cache")
            return data[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            data[key] = res
            return res
    return wrapper

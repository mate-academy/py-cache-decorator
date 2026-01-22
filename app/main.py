from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()), func.__name__)
        if key in result:
            print("Getting from cache")
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")

        return result[key]

    return wrapper

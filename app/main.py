from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result[key] = func(*args, **kwargs)
        return result[key]
    return wrapper

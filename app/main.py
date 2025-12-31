from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> int | list:
        if result.get(args) is None:
            print("Calculating new result")
            result[args] = func(*args, **kwargs)
            return result[args]
        else:
            print("Getting from cache")
            return result[args]

    return wrapper

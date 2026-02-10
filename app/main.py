from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> int:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            result[args] = func(*args)
            print("Calculating new result")
            return result[args]
    return wrapper

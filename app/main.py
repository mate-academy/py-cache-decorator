from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> int:
        if args not in result:
            result[args] = func(*args)
            print("Calculating new result")
            return result[args]
        else:
            print("Getting from cache")
            return result[args]

    return wrapper

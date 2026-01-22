from typing import Callable


def cache(func: Callable) -> Callable:
    values = {}

    def wrapper(*args) -> int:
        if args in values.keys():
            print("Getting from cache")
            return values[args]

        print("Calculating new result")
        result = func(*args)
        values[args] = result
        return result
    return wrapper

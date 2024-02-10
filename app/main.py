from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args) -> Callable:
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            result = func(*args)
            data[args] = result
            print("Calculating new result")
            return result
    return wrapper

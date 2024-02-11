from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args) -> str:

        if args in data:
            print("Getting from cache")
        else:
            data[args] = func(*args)
            print("Calculating new result")
        return data[args]
    return wrapper

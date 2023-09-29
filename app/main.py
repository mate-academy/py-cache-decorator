from typing import Callable


def cache(func: Callable) -> Callable:
    stored_values = {}

    def wrapper(*args) -> int | list:

        if args in stored_values:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_values[args] = func(*args)

        return stored_values[args]

    return wrapper

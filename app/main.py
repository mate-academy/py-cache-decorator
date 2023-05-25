from typing import Callable


def cache(func: Callable) -> Callable:
    stored_data = {}

    def wrapper(*args) -> int:

        nonlocal stored_data

        if args not in stored_data:
            print("Calculating new result")
            stored_data[args] = func(*args)
            return stored_data[args]

        print("Getting from cache")
        return stored_data[args]

    return wrapper

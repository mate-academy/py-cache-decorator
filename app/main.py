from typing import Callable


def cache(func: Callable) -> Callable:

    storage = {}

    def wrapper(*args) -> Callable:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)
        return storage[args]

    return wrapper

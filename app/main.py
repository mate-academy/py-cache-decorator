from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            storage[args] = func(*args)
            print("Calculating new result")
            return storage[args]

    return wrapper

from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            result = func(*args)
            storage[args] = result
            print("Calculating new result")
            return result
    return wrapper

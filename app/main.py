from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: object) -> object:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result
    return wrapper

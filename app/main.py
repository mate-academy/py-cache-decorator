from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        item = (args, tuple(kwargs.items()))
        if item in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[item] = func(*args, **kwargs)
        return storage[item]
    return wrapper

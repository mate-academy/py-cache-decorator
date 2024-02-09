from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrap(*args) -> Callable:
        key = (func.__name__, args)
        if key not in storage:
            print("Calculating new result")
            storage[key] = func(*args)
        else:
            print("Getting from cache")
        return storage[key]

    return wrap

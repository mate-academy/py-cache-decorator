from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Callable:
        if (func.__name__, args) in storage:
            result = storage[(func.__name__, args)]
            print("Getting from cache")
        else:
            result = func(*args)
            storage[(func.__name__, args)] = result
            print("Calculating new result")
        return result

    return inner

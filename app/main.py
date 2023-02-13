from typing import Callable


def cache(func: Callable) -> Callable:

    storage = {}

    def inner(*args, **kwargs) -> Callable:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args, **kwargs)
        return storage[args]

    return inner

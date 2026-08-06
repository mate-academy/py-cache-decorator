from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in storage:
            storage[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[args]
    return inner

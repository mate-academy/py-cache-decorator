from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> int:
        nonlocal storage
        if args not in storage:
            print("Calculating new result")
            storage[args] = func(*args)
            return storage[args]
        else:
            print("Getting from cache")
            return storage[args]

    return inner

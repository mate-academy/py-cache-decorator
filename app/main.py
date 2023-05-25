from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> int:
        if args not in storage:
            print("Calculating new result")
            storage[args] = func(*args)
            return storage[args]
        print("Getting from cache")
        return storage[args]

    return inner

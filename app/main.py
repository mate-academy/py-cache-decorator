from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Callable:
        if args not in storage.keys():
            storage[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return storage[args]
    return inner

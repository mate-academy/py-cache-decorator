from typing import Callable, Any


def cache(func: Callable) -> Any:
    storage = {}

    def inner(*args) -> Callable:
        if args not in storage.keys():
            storage[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return storage[args]
    return inner

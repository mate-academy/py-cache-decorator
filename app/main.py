from typing import Callable, Any


def cache(func: Callable) -> Any:
    storage = {}

    def inner(*args) -> Any:
        if args not in storage:
            print("Calculating new result")
            storage[args] = func(*args)
            return storage[args]
        print("Getting from cache")
        return storage[args]
    return inner

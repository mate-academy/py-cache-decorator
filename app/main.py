from typing import Callable


def cache(func: Callable) -> None:
    storage = {}

    def wrapper(*args: Callable) -> None:
        if args not in storage:
            res = func(*args)
            storage.update({args: res})
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[args]
    return wrapper

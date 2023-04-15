from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage.get(args)
        else:
            print("Calculating new result")
            storage[args] = func(*args)
            return storage.get(args)

    return inner

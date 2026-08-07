from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in storage:
            storage[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[key]
    return inner

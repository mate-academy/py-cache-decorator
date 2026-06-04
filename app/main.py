from typing import Callable


def cache(func: Callable) -> Callable:

    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))

        if len(storage) == 0:
            storage[key] = func(*args, **kwargs)
            print("Calculating new result")
            return storage[key]
        else:
            if key in storage:
                print("Getting from cache")
                return storage[key]
            else:
                print("Calculating new result")
                storage[key] = func(*args, **kwargs)
                return storage[key]

    return wrapper

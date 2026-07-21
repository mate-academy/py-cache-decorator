from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> int:
        data = (args, tuple(sorted(kwargs.items())))

        for item in data:
            if item not in storage:
                print("Calculating new result")
                storage[item] = func(*args, **kwargs)
                return storage[item]
            else:
                print("Getting from cache")
                return storage[item]

    return inner

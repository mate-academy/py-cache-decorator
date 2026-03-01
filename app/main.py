from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return inner

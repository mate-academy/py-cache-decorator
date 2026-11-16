from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = str(args) + str(kwargs)
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result
    return wrapper

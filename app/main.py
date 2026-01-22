from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            result = func(*args)
            storage[args] = result
            print("Calculating new result")
            return storage[args]
    return wrapper

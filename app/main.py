from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key not in storage:
            storage[key] = func(*args, **kwargs)
            print("Calculating new result")

        else:
            print("Getting from cache")

        return storage[key]

    return wrapper

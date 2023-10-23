from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func, tuple(args), frozenset(kwargs.items()))

        if key in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[key] = func(*args, **kwargs)

        return storage[key]

    return wrapper

from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in storage:
            print("Calculating new result")
            storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return storage[key]
    return wrapper

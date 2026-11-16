from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        storage[key] = func(*args, **kwargs)
        return storage[key]
    return wrapper

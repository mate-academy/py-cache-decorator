from typing import Callable, Any


def cache(func: Callable) -> Callable:
    num_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key not in num_storage:
            print("Calculating new result")
            num_storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return num_storage[key]
    return wrapper

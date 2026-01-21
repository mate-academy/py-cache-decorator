from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, tuple(kwargs.items()))

        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper

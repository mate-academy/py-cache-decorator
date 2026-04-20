from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in stored_data:
            print("Getting from cache")
            return stored_data[key]

        print("Calculating new result")
        value = func(*args, **kwargs)
        stored_data[key] = value
        return value
    return wrapper

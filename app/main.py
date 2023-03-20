from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    def wrapper(*args: tuple) -> Any:
        if args in stored_data:
            print("Getting from cache")
        else:
            stored_data[args] = func(*args)
            print("Calculating new result")
        return stored_data[args]

    return wrapper

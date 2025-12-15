from typing import Callable, Any


def cache(func: Callable) -> Callable:

    data = {}

    def wrapper(*args) -> Any:
        if args in data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data[args] = func(*args)
        return data[args]
    return wrapper

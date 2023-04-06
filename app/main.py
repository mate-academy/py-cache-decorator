from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data: dict = {}

    def wrapper(*args) -> Any:

        if args not in data:
            print("Calculating new result")
            data[args] = func(*args)
        else:
            print("Getting from cache")

        return data[args]

    return wrapper

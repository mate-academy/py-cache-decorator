from typing import Callable


def cache(func: Callable) -> None:
    stored_values = {}

    def inner(*args, **kwargs) -> None:
        if args not in stored_values:
            stored_values[args] = func(*args, **kwargs)
            print("Calculating new result")
            return stored_values[args]
        else:
            print("Getting from cache")
            return stored_values[args]
    return inner

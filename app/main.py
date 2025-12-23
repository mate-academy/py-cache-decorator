from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args: Any) -> Callable:
        key = (args)
        if key in data:
            print("Getting from cache")
        else:
            data[key] = func(*args)
            print("Calculating new result")
        return data[key]

    return inner

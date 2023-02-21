from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args: tuple) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
        data[args] = func(*args)
        return data[args]
    return inner

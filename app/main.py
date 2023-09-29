from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args) -> int:
        if args in data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data[args] = func(*args)
        return data[args]
    return inner

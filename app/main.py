from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args) -> None:
        if args in data:
            print("Getting from cache")
            return data[args]
        print("Calculating new result")
        data[args] = func(*args)
        return data[args]
    return inner

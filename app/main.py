from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args) -> any:

        if args not in data:
            data[args] = func(*args)
            print("Calculating new result\n")
        elif args in data:
            print("Getting from cache\n")
        return data[args]

    return inner

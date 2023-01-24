from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args) -> Callable:

        if args in result:
            print("Getting from cache")

        else:
            print("Calculating new result")
            result[args] = func(*args)
        return result[args]

    return inner

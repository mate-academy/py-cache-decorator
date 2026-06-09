from typing import Callable


def cache(func: Callable) -> Callable:
    count = {}

    def inner(*args) -> str:
        if args in count:

            print("Getting from cache")
            return count[args]
        else:
            count[args] = func(*args)

            print("Calculating new result")
            return count[args]

    return count

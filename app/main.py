from typing import Callable


def cache(func: Callable) -> Callable:
    res = {}

    def inner(*args) -> Callable:
        if args not in res:
            print("Calculating new result")
            res[args] = func(*args)
            return res[args]
        else:
            print("Getting from cache")
            return res[args]

    return inner
